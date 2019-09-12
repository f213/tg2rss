from envparse import env
from scrapy.crawler import CrawlerProcess

from spiders.pmdaily import PmdailySpider

__all__ = [
    'crawl',
]

env.read_envfile()

settings = dict(  # settings are here to fail at import time
    ITEM_PIPELINES={
        'pipelines.RSSPipeline': 900,
    },
    FEED_FILE=env('FEED_FILE', cast=str),
    FEED_TITLE=env('FEED_TITLE', cast=str),
    FEED_DESCRIPTION=env('FEED_DESCRIPTION', cast=str),
    FEED_LINK=env('FEED_LINK', cast=str),
    LOG_LEVEL=env('LOG_LEVEL', cast=str, default='ERROR'),
    IGNORE_TITLES=env('IGNORE_TITLES', cast=list, subcast=str, default=[]),
)


def crawl():
    crawler = CrawlerProcess(settings)
    crawler.crawl(PmdailySpider)
    crawler.start()


if __name__ == '__main__':
    crawl()
