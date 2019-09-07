from src.spider.spider_66_ip import Spider66Ip

DB_TYPE = 'memory'      # memory/redis

SPIDER_LIST = [Spider66Ip]


HEADERS = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}