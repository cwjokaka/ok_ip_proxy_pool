spider_collection = {}


def spider_register(cls):
    spider_collection.update({cls.__name__: cls})
    print(f'注册{cls.__name__}')
    return cls
