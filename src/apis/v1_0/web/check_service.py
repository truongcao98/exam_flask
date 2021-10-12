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

checking_service_mod = Blueprint("check_service", __name__)


@checking_service_mod.route(URI.PING, methods=[HTTP.METHOD.GET])
def check_service_online():
    return 'request successful cao lai truong!!! v1.0'






