from src.apis.v1_0.exam_blueprint import *


application = app

# @application.route('/static/<path:filename>')
# def send_attachment(filename):
#     resource_folder = SHARE_FOLDER_STATIC
#     return send_from_directory(resource_folder, filename)


@application.before_request
def execute_before_request():
    """
    Thực thi trước khi xử lý request. Ví dụ: kết nối database.
    :return:
    """
    pass


@application.after_request
def execute_after_request(response):
    return response


@application.teardown_request
def execute_when(exec):
    """
    Thực thi khi một request bị ngắt. Ví dụ: ngắt kết nối database.
    :param exec:
    :return:
    """


if __name__ == '__main__':
    application.run(host='127.0.0.1', port=5001, debug=True)
