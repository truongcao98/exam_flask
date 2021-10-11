from src.models.mongo.congviec import CVCollection
from flask import request
import pymongo
from bson.json_util import dumps
from bson.json_util import loads


class CongviecController:
    def add_congviec(self):
        data = request.get_json()
        CVCollection().insert(data)

    def remove_congviec(self):
        print(request.get_json())
        data = request.get_json()
        # param = request.args.get("name")
        # print(param)
        CVCollection().delete_one(data)

    def update_congviec(self):
        print(request.get_json())
        data = request.get_json()
        CVCollection().update(data['filter_option'], data['update_option'])

    def select_all_congviec(self, projection=None):
        data = request.get_json()
        search_option = data['search_option']
        projection = {'fisrt name': 0, }
        results = CVCollection().select_all(search_option, projection)
        result = list()
        for i in results:
            nv_id = str(i.get("_id"))
            i["_id"] = nv_id
            result.append(i)
        return result

    def find_one_congviec(self):
        data = request.get_json()
        search_option = data['search_option']
        results = CVCollection().select_all(search_option)
        result = list()
        for i in results:
            nv_id = str(i.get("_id"))
            i["_id"] = nv_id
            result.append(i)
        return result
