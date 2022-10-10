from src.redis_client import redis_client
from redis_lru import RedisLRU
import json

cache = RedisLRU(redis_client)

# redis_client.flushdb()


def show_cache():
    for key in redis_client.scan_iter():
        print('Key:', key)
        print('Value:', redis_client.get(key))


class LruCache:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        key = args[0]
        if cache.get(key) is not None:
            value_json = cache.get(key)
            value = json.loads(value_json)
            print(value)
            show_cache()
        else:
            value = self.func(*args, **kwargs)
            value_json = json.dumps(value)
            cache.set(key, value_json)
            print(value)
            show_cache()
