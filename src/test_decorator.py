def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


if __name__ == '__main__':
    say_hello()
