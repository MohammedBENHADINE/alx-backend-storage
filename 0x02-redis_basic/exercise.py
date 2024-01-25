#!/usr/bin/env python3
"""create class to instantiate redis"""
import redis
import uuid
from typing import Union


class Cache:
    """class Cache that make a cash mem"""

    def __init__(self):
        """main constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
