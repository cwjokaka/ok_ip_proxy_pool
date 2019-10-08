# ok_ip_proxy_pool😁
一个还ok的IP代理池,先做给自己用着~



## 运行环境

- python 3.7



## 特点

- 异步爬取&验证代理🚀
- 用权重加减来衡量代理的可用性(可用性:通过验证则+1,否则-1)🎭
- 使用Sqlite,无需安装数据库环境🛴
- 目前支持的免费代理有: 免费代理/全网/66/西刺/快代理/云代理/IP海



## 下载&安装

- 源码下载:

  ```
  git clone git@github.com:cwjokaka/ok_ip_proxy_pool.git
  ```

  

- 安装依赖:

  ```
  pip install -r requirements.txt
  ```



## 配置文件
```python
# 代理爬虫配置
SPIDER = {
    'crawl_interval': 120,       # 爬取IP代理的间隔(秒)
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
    'test_url': 'http://www.baidu.com',     # 可用校验url
    'request_timeout': 4,           # 校验超时时间
    'validate_interval': 60         # 校验间隔(秒)
}

# 匿名性校验配置
ANONYMITY_VALIDATOR = {
    'http_test_url': 'http://httpbin.org/get',      # 匿名校验url
    'https_test_url': 'https://httpbin.org/get',
    'request_timeout': 4,                           # 校验最大超时时间
    'interval': 180                                 # 校验间隔(秒)
}

# 数据库配置
DB = {
    'db_name': 'proxy.db',
    'table_name': 'proxy'
}

# WEB配置(Flask)
WEB_SERVER = {
    'host': '0.0.0.0',
    'port': '8080'
}

# 爬虫请求头
HEADERS = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}
```





## 运行
  ```
  python main.py
  ```





## API使用

|   API    | method | description  |
| :------: | :----: | :----------: |
|    /     |  GET   |   首页介绍   |
|   /get   |  GET   | 获取一个代理 |
| /get_all |  GET   | 获取所有代理 |



## 代理爬虫扩展
如果需要添加自定义代理爬虫,可通过以下步骤添加:

1. 进入src/spider/spiders.py
2. 添加自己的爬虫类，继承AbsSpider，实现它的do_crawl & get_page_range & get_urls方法，按需重写其他方法。
3. 用@spider_register修饰此类
4. 在配置文件setting.py的SPIDER['list']中添加此类名



## LAST

欢迎Fork|Star|Issue 三连😘
