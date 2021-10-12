import json

from flask import Blueprint

from src.apis import HTTP
from src.apis.uri import URI
from src.controllers.v1_0.task_controller import TaskController

task_service_mod = Blueprint("task", __name__)


@task_service_mod.route(URI.ADD_TASK, methods=[HTTP.METHOD.POST])
def add_task():
    TaskController().add_task()
    return 'success'


@task_service_mod.route(URI.REMOVE_TASK, methods=[HTTP.METHOD.POST])
def remove_task():
    # print(data)
    TaskController().remove_task()
    return 'success'


@task_service_mod.route(URI.UPDATE_TASK, methods=[HTTP.METHOD.POST])
def update_task():
    # print(data)
    TaskController().update_task()
    return 'success'


@task_service_mod.route(URI.SELECT_ALL_TASK, methods=[HTTP.METHOD.GET])
def select_all_task():
    # print(data)
    result = TaskController().select_all_task()
    return json.dumps(result)


@task_service_mod.route(URI.FIND_ONE_TASK, methods=[HTTP.METHOD.GET])
def find_one_task():
    # print(data)
    result = TaskController().find_one_task()
    return json.dumps(result)


@task_service_mod.route(URI.ADD_MANY, methods=[HTTP.METHOD.POST])
def add_many_task():
    TaskController().add_many_task()
    return 'success'
