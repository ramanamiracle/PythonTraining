# Python program showing
# class decorator with *args
# and **kwargs

class MyDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        # We can add some code
        # before function call

        self.function(*args, **kwargs)

        # We can also add some code
        # after function call.


# adding class decorator to the function
@MyDecorator
def function(name, message='Hello'):
    print("{}, {}".format(message, name))


function("geeks_for_geeks", "hello")


class SquareDecorator:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        # before function
        result = self.function(*args, **kwargs)

        # after function
        return result

        # adding class decorator to the function


@SquareDecorator
def get_square(n):
    print("given number is:", n)
    return n * n


print("Square of number is:", get_square(195))

from time import time

class Timer:
    def __init__(self, func):
        self.function = func

    def __call__(self, *args, **kwargs):
        start_time = time()
        result = self.function(*args, **kwargs)
        end_time = time()
        print("Execution took {} seconds".format(end_time - start_time))
        return result

    # adding a decorator to the function


@Timer
def some_function(delay):
    from time import sleep

    # Introducing some time delay to
    # simulate a time taking function.
    sleep(delay)


some_function(3)