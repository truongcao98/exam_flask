#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Author: ChungNT
    Company: MobioVN
    Date created: 29/06/2018
"""
import json

from flask import Blueprint, Response

from src.apis import HTTP
from src.apis.uri import URI

checking_service_mod = Blueprint("check_service", __name__)


@checking_service_mod.route(URI.PING, methods=[HTTP.METHOD.GET])
def check_service_online():
    return 'request successful!!! v1.0'


@checking_service_mod.route(URI.VIETNAMESE_CHECK, methods=[HTTP.METHOD.GET])
def check_vietnamese_support():
    """
    Endpoint to demonstrate Vietnamese language support
    Responds to the question: "Bạn có hiểu tiếng Việt không?" (Do you understand Vietnamese?)
    """
    response = {
        "question": "Bạn có hiểu tiếng Việt không?",
        "answer": "Có, tôi hiểu tiếng Việt!",
        "translation": {
            "question_en": "Do you understand Vietnamese?",
            "answer_en": "Yes, I understand Vietnamese!"
        },
        "message": "Ứng dụng Flask này hỗ trợ tiếng Việt hoàn toàn",
        "features": [
            "Hỗ trợ văn bản tiếng Việt",
            "Có thể xử lý dữ liệu có dấu",
            "Tương thích với MongoDB UTF-8"
        ]
    }
    json_response = json.dumps(response, ensure_ascii=False, indent=2)
    return Response(json_response, content_type='application/json; charset=utf-8')






