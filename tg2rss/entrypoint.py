import time

import schedule

from crawl import crawl


def _crawl():
    print('Running crawling...')  # noqa
    crawl()
    print('Crawling done!')  # noqa


if __name__ == '__main__':
    schedule.every().minute.do(_crawl)

    while True:
        schedule.run_pending()
        time.sleep(1)