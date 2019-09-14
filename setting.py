DB_CONFIG = {
    'db_type': 'MemoryDB',     # memory/redis
    'url': '',
    'username': 'root',
    'password': 'root'
}

SPIDER_LIST = [
    'Spider66Ip',
    'SpiderQuanWangIp',
    'SpiderXiciIp'
]

# 爬虫请求头
HEADERS = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}