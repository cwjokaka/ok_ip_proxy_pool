import asyncio
import typing
from asyncio import AbstractEventLoop

from src.database.memory_db import db_collection
from src.entity.proxy_entity import ProxyEntity
from src.spider.spiders import spider_collection
from setting import SPIDER_LIST, DB_CONFIG
from threading import Thread


def crawl(event_loop: AbstractEventLoop):
    proxies = []
    for spider_name in SPIDER_LIST:
        proxies.extend(spider_collection[spider_name].crawl(event_loop))
    return proxies


def save(proxies: typing.List[ProxyEntity]):
    db = db_collection[DB_CONFIG['db_type']]
    for proxy in proxies:
        db.set(f'{proxy.ip}:{proxy.port}', proxy)


def start_event_loop(loop):
    def init_loop(_loop):
        asyncio.set_event_loop(_loop)
        _loop.run_forever()
    loop_thread = Thread(target=init_loop, args=(loop,))
    loop_thread.setDaemon(True)
    loop_thread.start()


if __name__ == '__main__':
    new_loop = asyncio.new_event_loop()
    start_event_loop(new_loop)

    # 爬取
    proxies = crawl(new_loop)
    # 持久化
    # save(proxies)
    print()
