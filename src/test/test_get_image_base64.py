import base64
import requests


class Test:
    def __init__(self):
        pass

    @staticmethod
    def get_as_base64(url):
        return base64.b64encode(requests.get(url).content)


if __name__ == '__main__':
    url = 'https://t1.mobio.vn/static/1b99bdcf-d582-4f49-9715-1b61dfff3924/upload/62a9bf415ac95f99b7863800.jpg'
    truongcl = Test.get_as_base64(url)
    print('truongcl')