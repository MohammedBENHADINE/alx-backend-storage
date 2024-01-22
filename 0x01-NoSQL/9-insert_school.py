#!/usr/bin/env python3
"""this function create a new doc"""


def insert_school(mongo_collection, **kwargs):
    """a Python function that create a new doc"""
    return mongo_collection.insert_one(kwargs).inserted_id