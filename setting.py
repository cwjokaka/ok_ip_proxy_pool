# from src.spider.spider_66_ip import Spider66Ip
# from src.spider.spider_quan_wang_ip import SpiderQuanWangIp
from src.database.memory_db import *

DB = {
    'db_typy': 'memory'     # memory/redis
}

# SPIDER_LIST = [Spider66Ip, SpiderQuanWangIp]


# 爬虫请求头
HEADERS = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}