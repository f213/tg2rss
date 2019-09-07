import re
from hashlib import sha256
from typing import Optional

import scrapy
from scrapy_rss import RssItem


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = [
        't.me',
    ]

    start_urls = [
        'https://t.me/s/pmdaily/',
    ]

    def parse(self, response):
        for item in response.css('.tgme_widget_message'):
            post = Post(item)
            if post.title is None or len(post.title) < 3:
                continue

            item = RssItem()
            item.link = post.link
            item.title = post.title
            item.description = post.text
            item.guid = post.id
            if post.img is not None:
                item.enclosure = dict(url=post.img, type='image/jpeg')

            yield item


class Post:
    def __init__(self, post):
        self.post = post

    @property
    def _title(self):
        return self.post.css('.tgme_widget_message_text b:first-child')

    @property
    def title(self) -> Optional[str]:
        """First bold line of the text"""
        title = self._title.css('::text').extract_first()
        if title is not None and len(title) >= 3:
            return title

    @property
    def id(self) -> str:
        """Unique id based on the post URL"""
        url = self.post.css('::attr(data-post)').extract_first()

        return sha256(url.encode()).hexdigest()

    @property
    def link(self) -> str:
        return 'https://t.me/s/' + self.post.css('::attr(data-post)').extract_first()

    @property
    def img(self) -> Optional[str]:
        """Take img from link preview image"""
        styles = self.post.css('.tgme_widget_message_link_preview i::attr(style)').extract_first()
        if styles is None:
            return

        for style in styles.split(';'):
            if style.startswith('background-image:url'):
                return style.replace("background-image:url('", '').replace("')", '')

    @property
    def text(self) -> str:
        paragraphs = self.paragraphs
        if paragraphs[0] == self.title:
            del paragraphs[0]

        return "\n\n".join(paragraphs)

    @property
    def paragraphs(self) -> str:
        """Post text split to paragraphs"""
        raw = self.post.css('.tgme_widget_message_text').extract_first()

        return [self.strip_tags(line) for line in raw.split('<br><br>')]

    @staticmethod
    def strip_tags(line):
        return re.sub(r'<[^<>]+>', '', line)
