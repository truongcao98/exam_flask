import json
from src.apis import HTTP
from src.apis.uri import URI
from src.controllers.v1_0.staff_controller import StaffController
from flask import Blueprint

staff_service_mod = Blueprint("staff", __name__)


@staff_service_mod.route(URI.ADD_STAFF, methods=[HTTP.METHOD.POST])
def add_staff():
    StaffController().add_staff()
    return 'success'


@staff_service_mod.route(URI.REMOVE_STAFF, methods=[HTTP.METHOD.POST])
def remove_staff():
    # print(data)
    StaffController().remove_staff()
    return 'success'


@staff_service_mod.route(URI.UPDATE_STAFF, methods=[HTTP.METHOD.POST])
def update_staff():
    # print(data)
    StaffController().update_staff()
    return 'success'


@staff_service_mod.route(URI.SELECT_ALL_STAFF, methods=[HTTP.METHOD.GET])
def select_all_staff():
    # print(data)
    result = StaffController().select_all_staff()
    return json.dumps(result)


@staff_service_mod.route(URI.FIND_ONE_STAFF, methods=[HTTP.METHOD.GET])
def find_one_staff():
    # print(data)
    result = StaffController().find_one_staff()
    return json.dumps(result)
