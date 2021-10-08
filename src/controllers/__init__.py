#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Author: ThongNV
    Company: MobioVN
    Date created: 27/11/2019
"""


class CommonParams:
    LANGUAGE = 'lang'
    PAGE = 'page'
    PER_PAGE = 'per_page'
    ORDER = 'order'
    SORT = 'sort'
    TOTAL_ITEM = 'total_item'
    TOTAL_PAGE = 'total_page'
    AFTER_TOKEN = 'after_token'
    BEFORE_TOKEN = 'before_token'
    X_Merchant_ID = 'X-Merchant-ID'
    MERCHANT_ID = 'merchant_id'
    MERCHANT_IDS = 'merchant_ids'


class Params:
    CREATED_TIME = 'created_time'
    SORT = 'sort'
    ORDER = 'order'


class RequeueStatus:
    ENABLE = 0
    DISABLE = -1
