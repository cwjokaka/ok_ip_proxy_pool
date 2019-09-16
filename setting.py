SPIDER = {
    'crawl_interval': 60,       # 爬取IP代理的间隔(秒)
    'list': [
        'Spider66Ip',
        'SpiderQuanWangIp',
        'SpiderXiciIp',
        'SpiderKuaiDaiLiIp'
    ]
}

VALIDATOR = {
    'test_url': 'https://www.baidu.com',
    'request_timeout': 4,
    'validate_interval': 60
}

# sqlite
DB = {
    'db_name': 'test.db',
    'table_name': 'proxy'
}

WEB_SERVER = {
    'host': 'localhost',
    'port': '8080'
}

# 爬虫请求头
HEADERS = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}