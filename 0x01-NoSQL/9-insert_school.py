#!/usr/bin/env python3
"""this function create a new doc"""


def insert_school(mongo_collection, **kwargs):
    """a Python function that create a new doc"""
    new_doc = {}
    for key, value in kwargs.items():
        new_doc[key] = value
    return mongo_collection.insert_one(new_doc)
