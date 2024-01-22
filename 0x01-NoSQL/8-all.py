#!/usr/bin/env python3
"""this function list all doc in a collection"""


def list_all(mongo_collection):
    """a Python function that lists all documents in a collection"""
    return mongo_collection.find()
