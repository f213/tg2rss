
from feedgen.feed import FeedGenerator


class RSSPipeline:
    def open_spider(self, spider):
        self.settings = spider.settings

        self.feed = self.get_feed()

    def close_spider(self, spider):
        self.feed.rss_file(self.settings['FEED_FILE'])

    def process_item(self, item, spider):
        entry = self.feed.add_entry()

        entry.id(item['guid'])
        entry.title(item['title'])
        entry.link(href=item['link'])
        entry.description('')
        entry.content(item['description'], type='CDATA')
        if item.get('enclosure'):
            entry.enclosure(**item['enclosure'], length='100500')

    def get_feed(self):
        feed = FeedGenerator()
        feed.title('Scraped RSS Feed')
        feed.link(href=self.settings['FEED_LINK'])
        feed.description(self.settings['FEED_DESCRIPTION'])

        return feed
