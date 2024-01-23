#!/usr/bin/env python3
"""list of schools with specific topic"""


def schools_by_topic(mongo_collection, topic):
    """a Python function that finds schools by topic"""
    return mongo_collection.find({"topics": topic})