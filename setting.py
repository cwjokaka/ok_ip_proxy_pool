# 代理爬虫配置
SPIDER = {
    'crawl_interval': 60,       # 爬取IP代理的间隔(秒)
    'list': [                   # 使用的代理爬虫(类名)
        'Spider66Ip',
        'SpiderQuanWangIp',
        'SpiderXiciIp',
        'SpiderKuaiDaiLiIp',
        'SpiderYunDaiLiIp',
        'SpiderIpHaiIp',
        'SpiderMianFeiDaiLiIp'
    ]
}

# 校验器配置
VALIDATOR = {
    'test_url': 'http://www.baidu.com',
    'request_timeout': 4,           # 校验超时时间
    'validate_interval': 30
}

# 数据库配置
DB = {
    'db_name': 'test.db',
    'table_name': 'proxy'
}

# WEB配置(Flask)
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