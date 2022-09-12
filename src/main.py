# https://github.com/redis/redis-py/blob/master/tests/test_bloom.py

import redis
from redis.commands.bf import BFBloom

client = redis.Redis(host="redis", port=6379, db=0)
bf: BFBloom = client.bf()
