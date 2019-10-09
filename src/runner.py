import asyncio
import typing

from apscheduler.schedulers.background import BackgroundScheduler

from src.database.sqlite_opt import sqlite_opt
from src.entity.proxy_entity import ProxyEntity
from src.log.logger import logger
from src.spider.spiders import spider_collection
from setting import WEB_SERVER, VALIDATOR, SPIDER, ANONYMITY_VALIDATOR, EXPIRATION_VALIDATOR
from src.validator.expiration_validator import expiration_validator
from src.validator.validator import validator
from src.validator.anonymity_validator import anonymity_validator
from src.web.web_flask import app


def crawl():
    proxies = []
    tasks = []
    for spider_name in SPIDER['list']:
        tasks.append(spider_collection[spider_name].crawl())
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    results = loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
    for proxies_list in results:
        proxies.extend(proxies_list)
    # proxies = loop.run_until_complete(asyncio.gather(*tasks))
    # 持久化
    save(proxies)


def save(proxies: typing.List[ProxyEntity]):
    for proxy in proxies:
        sqlite_opt.add_proxy(proxy)


def run():
    logger.info('初始化sqlite数据库...')
    sqlite_opt.init_db()
    scheduler = BackgroundScheduler()
    scheduler.add_job(crawl, 'interval', seconds=SPIDER['crawl_interval'])
    scheduler.add_job(validator.run, 'interval', seconds=VALIDATOR['validate_interval'])
    scheduler.add_job(anonymity_validator.run, 'interval', seconds=ANONYMITY_VALIDATOR['interval'])
    scheduler.add_job(expiration_validator.run, 'interval', seconds=EXPIRATION_VALIDATOR['interval'])
    scheduler.start()
    app.run(host=WEB_SERVER['host'], port=WEB_SERVER['port'])
