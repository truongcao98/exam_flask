from src.models.mongo.nhanvien import NVCollection
from flask import request
import pymongo
from bson.json_util import dumps
from bson.json_util import loads


class NhanvienController():
    def add_nhanvien(self):
        data = request.get_json()
        NVCollection().insert(data)

    def remove_nhanvien(self):
        print(request.get_json())
        data = request.get_json()
        # param = request.args.get("name")
        # print(param)
        NVCollection().delete_one(data)

    def update_nhanvien(self):
        print(request.get_json())
        data = request.get_json()
        NVCollection().update(data['filter_option'], data['update_option'])

    def select_all_nhanvien(self, projection=None):
        data = request.get_json()
        search_option = data['search_option']
        projection = {'fisrt name': 0, }
        results = NVCollection().select_all(search_option, projection)
        result = list()
        for i in results:
            nv_id = str(i.get("_id"))
            i["_id"] = nv_id
            result.append(i)
        return result

    def find_one_nhanvien(self):
        data = request.get_json()
        search_option = data['search_option']
        results = NVCollection().select_all(search_option)
        result = list()
        for i in results:
            nv_id = str(i.get("_id"))
            i["_id"] = nv_id
            result.append(i)
        return result
