from flask import Flask


class HTTP:
    class METHOD:
        DELETE = 'delete'
        PATCH = 'patch'
        PUT = 'put'
        POST = 'post'
        GET = 'get'

    class STATUS:
        OK = 200


app = Flask(__name__, static_folder=None)
