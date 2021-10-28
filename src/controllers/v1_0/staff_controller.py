from flask import request

from src.models.mongo.staff import StaffCollection


class StaffController():
    def add_staff(self):
        data = request.get_json()
        StaffCollection().insert(data)

    def remove_staff(self):
        print(request.get_json())
        data = request.get_json()
        # param = request.args.get("name")
        # print(param)
        StaffCollection().delete_one(data)

    def update_staff(self):
        print(request.get_json())
        data = request.get_json()
        StaffCollection().update(data['filter_option'], data['update_option'])

    def select_all_staff(self, projection=None):
        data = request.get_json()
        search_option = data['search_option']
        projection = {'fisrt name': 0, }
        results = StaffCollection().select_all(search_option, projection)
        result = list()
        for i in results:
            nv_id = str(i.get("_id"))
            i["_id"] = nv_id
            result.append(i)
        return result

    def find_one_staff(self):
        data = request.get_json()
        search_option = data['search_option']
        results = StaffCollection().select_all(search_option)
        result = list()
        for i in results:
            nv_id = str(i.get("_id"))
            i["_id"] = nv_id
            result.append(i)
        return result
