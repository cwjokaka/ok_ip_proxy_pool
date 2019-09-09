import typing

from src.database.memory_db import db_collection
from src.entity.proxy_entity import ProxyEntity
from src.spider.spiders import spider_collection
from setting import SPIDER_LIST, DB_CONFIG


def crawl():
    proxies = []
    for spider_name in SPIDER_LIST:
        proxies.extend(spider_collection[spider_name].crawl())
    return proxies


def save(proxies: typing.List[ProxyEntity]):
    db = db_collection[DB_CONFIG['db_type']]
    for proxy in proxies:
        db.set(f'{proxy.ip}:{proxy.port}', proxy)





if __name__ == '__main__':
    proxies = crawl()
    # 爬取
    save(proxies)
    # 持久化
    print()
