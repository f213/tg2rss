import time
from os import path, system

import schedule


def _crawl():
    print('Running crawl')  # noqa
    crawler_path = path.join(path.dirname(__file__), 'crawl.py')

    system(f'python {crawler_path}')


if __name__ == '__main__':
    _crawl()  # do crawling at the first run

    schedule.every().hour.do(_crawl)

    while True:
        schedule.run_pending()
        time.sleep(1)
