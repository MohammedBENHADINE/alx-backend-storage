#!/usr/bin/env python3
"""get resume from logs"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs.nginx
    logs = db.count_documents({})
    print("{} logs".format(logs))
    print("Methods:")
    print("\tmethod GET: {}".format(db.count_documents({"method": "GET"})))
    print("\tmethod POST: {}".format(db.count_documents({"method": "POST"})))
    print("\tmethod PUT: {}".format(db.count_documents({"method": "PUT"})))
    print("\tmethod PATCH: {}".format(db.count_documents({"method": "PATCH"})))
    print("\tmethod DELETE: {}".format(db.count_documents(
        {"method": "DELETE"}
    )))
    print("{} status check".format(db.count_documents(
        {"method": "GET", "path": "/status"}
    )))
