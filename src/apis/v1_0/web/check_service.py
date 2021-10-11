#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Author: ChungNT
    Company: MobioVN
    Date created: 29/06/2018
"""
import json

from flask import Blueprint

from src.apis import HTTP
from src.apis.uri import URI
from src.controllers.v1_0.nhanvien_controller import NhanvienController
from src.controllers.v1_0.congviec_controller import CongviecController

checking_service_mod = Blueprint("check_service", __name__)


@checking_service_mod.route(URI.PING, methods=[HTTP.METHOD.GET])
def check_service_online():
    return 'request successful cao lai truong!!! v1.0'


@checking_service_mod.route(URI.ADD_NHANVIEN, methods=[HTTP.METHOD.POST])
def add_nhanvien():
    NhanvienController().add_nhanvien()
    return 'successfull'


@checking_service_mod.route(URI.REMOVE_NHANVIEN, methods=[HTTP.METHOD.POST])
def remove_nhanvien():
    # print(data)
    NhanvienController().remove_nhanvien()
    return 'successfull'


@checking_service_mod.route(URI.UPDATE_NHANVIEN, methods=[HTTP.METHOD.POST])
def update_nhanvien():
    # print(data)
    NhanvienController().update_nhanvien()
    return 'successfull'

@checking_service_mod.route(URI.SELECT_ALL_NHANVIEN, methods=[HTTP.METHOD.GET])
def select_all_nhanvien():
    # print(data)
    result = NhanvienController().select_all_nhanvien()
    return json.dumps(result)


@checking_service_mod.route(URI.FIND_ONE_NHANVIEN, methods=[HTTP.METHOD.GET])
def find_one_nhanvien():
    # print(data)
    result = NhanvienController().find_one_nhanvien()
    return json.dumps(result)

#CONGVIEC

@checking_service_mod.route(URI.ADD_CONGVIEC, methods=[HTTP.METHOD.POST])
def add_congviec():
    CongviecController().add_congviec()
    return 'successfull'


@checking_service_mod.route(URI.REMOVE_CONGVIEC, methods=[HTTP.METHOD.POST])
def remove_congviec():
    # print(data)
    CongviecController().remove_congviec()
    return 'successfull'


@checking_service_mod.route(URI.UPDATE_CONGVIEC, methods=[HTTP.METHOD.POST])
def update_congviec():
    # print(data)
    CongviecController().update_congviec()
    return 'successfull'

@checking_service_mod.route(URI.SELECT_ALL_CONGVIEC, methods=[HTTP.METHOD.GET])
def select_all_congviec():
    # print(data)
    result = CongviecController().select_all_congviec()
    return json.dumps(result)


@checking_service_mod.route(URI.FIND_ONE_CONGVIEC, methods=[HTTP.METHOD.GET])
def find_one_congviec():
    # print(data)
    result = CongviecController().find_one_congviec()
    return json.dumps(result)

