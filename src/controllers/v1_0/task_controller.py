from flask import request

from src.models.mongo.task import TaskCollection
from src.producer import Producer


class TaskController:
    @staticmethod
    def add_task():
        data = request.get_json()
        TaskCollection().insert(data)

    @staticmethod
    def add_many_task():
        data = request.get_json()
        print(data)
        Producer.push_data_to_kafka(data)

    @staticmethod
    def remove_task(self):
        print(request.get_json())
        data = request.get_json()
        # param = request.args.get("name")
        # print(param)
        TaskCollection().delete_one(data)

    @staticmethod
    def update_task(self):
        print(request.get_json())
        data = request.get_json()
        TaskCollection().update(data['filter_option'], data['update_option'])

    @staticmethod
    def select_all_task(self, projection=None):
        data = request.get_json()
        search_option = data['search_option']
        projection = {'fisrt name': 0, }
        results = TaskCollection().select_all(search_option, projection)
        result = list()
        for i in results:
            nv_id = str(i.get("_id"))
            i["_id"] = nv_id
            result.append(i)
        return result

    @staticmethod
    def find_one_task(self):
        data = request.get_json()
        search_option = data['search_option']
        results = TaskCollection().select_all(search_option)
        result = list()
        for i in results:
            nv_id = str(i.get("_id"))
            i["_id"] = nv_id
            result.append(i)
        return result
