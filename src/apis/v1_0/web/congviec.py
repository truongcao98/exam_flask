import json

from flask import Blueprint

from src.apis import HTTP
from src.apis.uri import URI
from src.controllers.v1_0.congviec_controller import CongviecController

congviec_service_mod = Blueprint("congviec", __name__)


@congviec_service_mod.route(URI.ADD_CONGVIEC, methods=[HTTP.METHOD.POST])
def add_congviec():
    CongviecController().add_congviec()
    return 'success'


@congviec_service_mod.route(URI.REMOVE_CONGVIEC, methods=[HTTP.METHOD.POST])
def remove_congviec():
    # print(data)
    CongviecController().remove_congviec()
    return 'success'


@congviec_service_mod.route(URI.UPDATE_CONGVIEC, methods=[HTTP.METHOD.POST])
def update_congviec():
    # print(data)
    CongviecController().update_congviec()
    return 'success'


@congviec_service_mod.route(URI.SELECT_ALL_CONGVIEC, methods=[HTTP.METHOD.GET])
def select_all_congviec():
    # print(data)
    result = CongviecController().select_all_congviec()
    return json.dumps(result)


@congviec_service_mod.route(URI.FIND_ONE_CONGVIEC, methods=[HTTP.METHOD.GET])
def find_one_congviec():
    # print(data)
    result = CongviecController().find_one_congviec()
    return json.dumps(result)


@congviec_service_mod.route(URI.ADD_MANY, methods=[HTTP.METHOD.POST])
def add_many_congviec():
    CongviecController().add_many_congviec()
    return 'success'
