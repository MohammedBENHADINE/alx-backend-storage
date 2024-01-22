#!/usr/bin/env python3
"""this function list all doc in a collection"""


def list_all(mongo_collection):
    docs = mongo_collection.find()
    if docs:
        return docs
    else:
        return []
