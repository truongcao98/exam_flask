def my_wrapper(func):
    def my_inner():
        print('inside wrapper')
        func('name')

    return my_inner()


@my_wrapper
def my_func_name(name):
    print('hello world')
    return 1


if __name__ == '__main__':
    my_func_name('truongcl')
