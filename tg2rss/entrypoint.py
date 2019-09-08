import time

import schedule

from crawl import crawl


def _crawl():
    print('Running crawling...')  # noqa
    crawl()


if __name__ == '__main__':
    _crawl()  # do crawling at the first run

    schedule.every().hour.do(_crawl)

    while True:
        schedule.run_pending()
        time.sleep(1)
