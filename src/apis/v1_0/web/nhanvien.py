import json
from src.apis import HTTP
from src.apis.uri import URI
from src.controllers.v1_0.nhanvien_controller import NhanvienController
from flask import Blueprint

nhanvien_service_mod = Blueprint("nhanvien", __name__)


@nhanvien_service_mod.route(URI.ADD_NHANVIEN, methods=[HTTP.METHOD.POST])
def add_nhanvien():
    NhanvienController().add_nhanvien()
    return 'success'


@nhanvien_service_mod.route(URI.REMOVE_NHANVIEN, methods=[HTTP.METHOD.POST])
def remove_nhanvien():
    # print(data)
    NhanvienController().remove_nhanvien()
    return 'success'


@nhanvien_service_mod.route(URI.UPDATE_NHANVIEN, methods=[HTTP.METHOD.POST])
def update_nhanvien():
    # print(data)
    NhanvienController().update_nhanvien()
    return 'success'


@nhanvien_service_mod.route(URI.SELECT_ALL_NHANVIEN, methods=[HTTP.METHOD.GET])
def select_all_nhanvien():
    # print(data)
    result = NhanvienController().select_all_nhanvien()
    return json.dumps(result)


@nhanvien_service_mod.route(URI.FIND_ONE_NHANVIEN, methods=[HTTP.METHOD.GET])
def find_one_nhanvien():
    # print(data)
    result = NhanvienController().find_one_nhanvien()
    return json.dumps(result)
