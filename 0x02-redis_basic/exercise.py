#!/usr/bin/env python3
"""create class to instantiate redis"""
import redis
import uuid


class Cache:
    """class Cache that make a cash mem"""

    def __init__(self):
        """main constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data):
        """store in redis"""
        key = uuid.uuid4()
        self._redis.set(str(key), str(data) if isinstance(data, str) else data)
        return str(key)
