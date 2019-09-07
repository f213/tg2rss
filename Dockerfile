FROM python:3.6.9-slim

RUN apt-get update \
    && apt-get --no-install-recommends install dumb-init \
    && rm -rf /var/lib/apt/lists/*

ADD requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

ADD tg2rss /srv

RUN mkdir -p /var/lib/tg2rss
VOLUME /var/lib/tg2rss

ENV FEED_FILE /var/lib/tg2rss/feed.rss
ENV FEED_TITLE Untitled RSS Feed
ENV FEED_DESRIPTION Empty
ENV FEED_LINK http://no.site

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

CMD python /srv/entrypoint.py
