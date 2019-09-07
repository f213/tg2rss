from scrapy.crawler import CrawlerProcess

from spiders.pmdaily import PmdailySpider


def crawl():
    crawler = CrawlerProcess(dict(
        ITEM_PIPELINES={
            'scrapy_rss.pipelines.RssExportPipeline': 900,
        },
        FEED_FILE='/tmp/feed.rss',
        FEED_TITLE='t.me/@pmdaily RSS feed',
        FEED_DESCRIPTION='',
        FEED_LINK='https://borshev.com/rss/tg/',
    ))

    crawler.crawl(PmdailySpider)
    crawler.start()


if __name__ == '__main__':
    crawl()
