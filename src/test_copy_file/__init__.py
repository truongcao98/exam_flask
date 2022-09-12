import shutil
from asyncore import dispatcher_with_send


class Test:
    def __init__(self):
        pass

    @staticmethod
    def copy_file(src, dst):
        shutil.copy2(src, dst)


if __name__ == '__main__':
    src = '/home/truongcl/test/exam_flask/src/folder_1/289738097_5502736383142274_5853309208829063372_n.jpg'
    dst = '/home/truongcl/test/exam_flask/src/folder_2/truongcl.jpg'
    Test().copy_file(src, dst)
