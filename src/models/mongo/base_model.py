#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
               ..
              ( '`<
               )(
        ( ----'  '.
        (         ;
         (_______,'
    ~^~^~^~^~^~^~^~^~^~^~
    Author: ThongNV
    Company: M O B I O
    Date Created: 8/2/21
"""
import uuid

from bson.objectid import ObjectId
from pymongo import MongoClient

# from src.apis import sys_conf

base_client = MongoClient('mongodb://admin:admin@localhost:27017/exam?authSource=admin')


class BaseModel:
    client = base_client
    db_name = 'exam'
    collection_name = ''

    def _db(self):
        return self.client[self.db_name]

    def get_db(self):
        db = self.client[self.db_name]
        collection = db[self.collection_name]
        return collection

    def insert(self, dictionary):
        db = self.client[self.db_name]
        return db[self.collection_name].insert_one(dictionary)

    def insert_many(self, document):
        db = self.client[self.db_name]
        return db[self.collection_name].insert_many(document)

    def update_one(self, id, dictionary):
        db = self.client[self.db_name]
        return db[self.collection_name].update_one(
            {"_id": self.normalize_object_id(id)},
            dictionary
        )

    def update_dictionary(self, id, dictionary):
        if isinstance(id, str):
            id = ObjectId(id)
        return self.collector().update_one({"_id": id}, dictionary)

    def update_one_query(self, query, data):
        return self.client.get_database(self.db_name)[self.collection_name].update_one(query,
                                                                                       {"$set": data}).matched_count

    def update_many(self, filter_option, update_option):
        db = self.client[self.db_name]
        db[self.collection_name].update_many(filter_option, update_option)

    def update(self, filter_option, update_option, upsert=False, multi=False):
        db = self.client[self.db_name]
        db[self.collection_name].update(filter_option, update_option, upsert=upsert, multi=multi)

    def update_by_set(self, filter_option, update_option, upsert=False, multi=False):
        db = self.client[self.db_name]
        db[self.collection_name].update(filter_option, {"$set": update_option}, upsert=upsert, multi=multi)

    def delete_one(self, delete_options):
        db = self.client[self.db_name]
        db[self.collection_name].delete_one(delete_options)

    def delete_many(self, delete_options):
        db = self.client[self.db_name]
        db[self.collection_name].delete_many(delete_options)

    def find_one(self, search_option):
        return self.collector().find_one(search_option)

    def collector(self):
        return self._db()[self.collection_name]

    def count_by_query(self, count_option):
        db = self.client[self.db_name]
        return db[self.collection_name].count(count_option)

    def count(self, search_option=None):
        if not search_option:
            search_option = {}
        return self._db()[self.collection_name].find(search_option).count()

    def select_all(self, search_option, projection=None):
        return self.collector().find(search_option, projection)
