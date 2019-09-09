import time
from os import system

import schedule


def _crawl():
    print('Running crawl')
    system('python crawl.py')


if __name__ == '__main__':
    _crawl()  # do crawling at the first run

    schedule.every().hour.do(_crawl)

    while True:
        schedule.run_pending()
        time.sleep(1)
