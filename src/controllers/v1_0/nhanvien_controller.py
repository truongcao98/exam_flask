from src.models.mongo.nhanvien import NVCollection
from flask import request


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




