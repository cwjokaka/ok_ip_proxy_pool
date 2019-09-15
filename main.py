import time
import typing

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.background import BackgroundScheduler

from src.database.sqlite_opt import sqlite_db
from src.entity.proxy_entity import ProxyEntity
from src.spider.spiders import spider_collection
from setting import SPIDER_LIST


def crawl():
    proxies = []
    for spider_name in SPIDER_LIST:
        proxies.extend(spider_collection[spider_name].crawl())
    # 持久化
    save(proxies)


def save(proxies: typing.List[ProxyEntity]):
    for proxy in proxies:
        sqlite_db.set(proxy)


def init_db():
    sqlite_db.init_db()


def check():
    print('开始检查')


if __name__ == '__main__':
    init_db()
    crawl()
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(crawl, 'interval', seconds=5)
    # scheduler.add_job(check, 'interval', seconds=5)
    # scheduler.start()
    # while True:
    #     print(time.time())
    #     time.sleep(5)
