import time
import typing

from apscheduler.schedulers.background import BackgroundScheduler

from src.database.sqlite_opt import sqlite_opt
from src.entity.proxy_entity import ProxyEntity
from src.spider.spiders import spider_collection
from setting import SPIDER_LIST
from src.validator.validator import validator


def crawl():
    proxies = []
    for spider_name in SPIDER_LIST:
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
    scheduler.add_job(crawl, 'interval', seconds=10)
    scheduler.add_job(check, 'interval', seconds=15)
    scheduler.start()
    while True:
        print(time.time())
        time.sleep(5)
