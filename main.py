import typing

from apscheduler.schedulers.background import BackgroundScheduler

from src.database.sqlite_opt import sqlite_opt
from src.entity.proxy_entity import ProxyEntity
from src.spider.spiders import spider_collection
from setting import WEB_SERVER, VALIDATOR, SPIDER
from src.validator.validator import validator
from src.web.web_flask import app


def crawl():
    proxies = []
    for spider_name in SPIDER['list']:
        proxies.extend(spider_collection[spider_name].crawl())
    # 持久化
    save(proxies)


def save(proxies: typing.List[ProxyEntity]):
    for proxy in proxies:
        sqlite_opt.add_proxy(proxy)


def init_db():
    sqlite_opt.init_db()


def check():
    validator.run()


if __name__ == '__main__':
    init_db()
    scheduler = BackgroundScheduler()
    scheduler.add_job(crawl, 'interval', seconds=SPIDER['crawl_interval'])
    scheduler.add_job(check, 'interval', seconds=60)
    scheduler.start()
    app.run(host=WEB_SERVER['host'], port=WEB_SERVER['port'])
