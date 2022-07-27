import sys


def hello():
    pass


if __name__ == '__main__':
    name_server = sys.argv[1]
    if name_server not in ['onpremise', 'cloud']:
        print('server must onpremise or cloud')

    merchant_id = sys.argv[2]
    if not merchant_id:
        print('miss merchant_id')
    print('name_server: ', name_server)
    print('merchant_id: ', merchant_id)
