import json

from flask import Blueprint

from src.apis import HTTP
from src.apis.uri import URI
from src.controllers.v1_0.staff_controller import StaffController

staff_service_mod = Blueprint("staff", __name__)


@staff_service_mod.route(URI.ADD_STAFF, methods=[HTTP.METHOD.POST])
def add_staff():
    StaffController().add_staff()
    return 'success'


@staff_service_mod.route(URI.REMOVE_STAFF, methods=[HTTP.METHOD.DELETE])
def remove_staff():
    StaffController().remove_staff()
    return 'success'


@staff_service_mod.route(URI.UPDATE_STAFF, methods=[HTTP.METHOD.PUT])
def update_staff():
    StaffController().update_staff()
    return 'success'


@staff_service_mod.route(URI.SELECT_ALL_STAFF, methods=[HTTP.METHOD.GET])
def select_all_staff():
    result = StaffController().select_all_staff()
    return json.dumps(result)


@staff_service_mod.route(URI.FIND_ONE_STAFF, methods=[HTTP.METHOD.GET])
def find_one_staff():
    result = StaffController().find_one_staff()
    return json.dumps(result)
