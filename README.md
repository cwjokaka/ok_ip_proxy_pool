# ok_ip_proxy_pool😁
一个还ok的IP代理池,先做给自己用着~



## 运行环境:

- python 3.7



## 特点

- 异步爬取&验证代理🚀
- 使用Sqlite,无需额外数据库环境🛴

- 目前支持的代理有: 免费代理/全网/66/西刺/快代理/云代理/IP海



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



## LAST

欢迎Fork|Star|Issue 三连😘
