# def get_name():
#     return 'func_get_name'
#
#
# def _get_name():
#     return 'private func_get_name'


class Func1:

    def __init__(self):
        self.name = 'truongcl'

    @staticmethod
    def get_name():
        return 'func_get_name'

    @staticmethod
    def _get_name():
        return 'private func_get_name'

    @staticmethod
    def __get_name():
        return 'private func_get_name 2'

    @staticmethod
    def kt():
        return Func1.__get_name()


if __name__ == '__main__':
    print(Func1().kt())
