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

from configs import Mongo
from src.apis import sys_conf

base_client = MongoClient(Mongo.MONGO_URI)


class BaseModel:
    client = base_client
    db_name = Mongo.DB
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

    def insert_document(self, dictionary):
        db = self.client[self.db_name]
        sys_conf.logger.debug('insert_document():insert:document: %s' % dictionary)
        return db[self.collection_name].insert_one(dictionary)

    def update_one(self, id, dictionary):
        db = self.client[self.db_name]
        return db[self.collection_name].update_one(
            {"_id": self.normalize_object_id(id)},
            dictionary
        )

    def update_set_dictionary(self, search_option, dictionary):
        db = self.client[self.db_name]

        document = db[self.collection_name].find_one(search_option)
        if document:
            sys_conf.logger.debug('update_one():update:document: %s' % dictionary)
            return db[self.collection_name].update_one(filter=search_option, update={'$set': dictionary},
                                                       upsert=True).matched_count >= 1
        return None

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

    def upsert(self, search_option, dictionary):
        db = self.client[self.db_name]
        out = True
        document = db[self.collection_name].find_one(search_option)
        if document:
            sys_conf.logger.debug('__init__::upsert():update:document: %s' % dictionary)
            document.update(dictionary)
            self.collector().replace_one({"_id": document.get('_id')}, dictionary, upsert=True)
            out = False
        else:
            sys_conf.logger.debug('__init__::upsert():insert:document: %s' % dictionary)
            db[self.collection_name].insert_one(dictionary)
        return out

    def find(self, search_option, obj_field_select: dict = None):
        db = self.client[self.db_name]
        if obj_field_select:
            sys_conf.logger.debug(
                'find():find:search_option: {} field_select: {}'.format(search_option, obj_field_select))
            return db[self.collection_name].find(search_option, obj_field_select)
        return db[self.collection_name].find(search_option)

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

    def find_paginate(self, search_option, page=0, per_page=None, sort_option=None, projection=None):
        collection = self.collector().find(search_option, projection)
        if sort_option:
            collection = collection.sort(sort_option)

        if page != -1:
            if per_page:
                collection = collection.limit(per_page)
            if page > 0:
                page -= 1
                offset = int(page) * int(per_page)
                collection = collection.skip(offset)

        return collection

    def _aggregate(self, group, match: object, sort=None, project=None):
        db = self.client[self.db_name]
        pipeline = []
        if match:
            pipeline.append({"$match": match})
        pipeline.append({"$group": group})
        if sort:
            pipeline.append({"$sort": sort})
        if project:
            pipeline.append({"$project": project})
        sys_conf.logger.debug('__init__::_aggregate():pipeline: %s' % pipeline)
        return db[self.collection_name].aggregate(pipeline)

    def distinct(self, fields, query):
        db = self.client[self.db_name]

        if type(fields) is str:
            return db[self.collection_name].distinct(fields, query)

        return None

    @staticmethod
    def normalize_uuid(some_uuid):
        if isinstance(some_uuid, str):
            return uuid.UUID(some_uuid)
        return some_uuid

    @staticmethod
    def normalize_object_id(some_object_id):
        if isinstance(some_object_id, str):
            return ObjectId(some_object_id)
        return some_object_id
