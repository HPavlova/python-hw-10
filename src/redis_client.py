import redis

redis_client = redis.Redis(
    host='localhost',
    port=6379,
    password=None
)

print(redis_client.info())
