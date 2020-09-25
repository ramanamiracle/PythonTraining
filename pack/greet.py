"""
greet
~~~~~
This module contains the greeting message 'msg' and greeting function 'greet()'.
"""
msg = "Hello"


def greet(name):  # Function
    """Do greeting"""
    print('{}, {}'.format(msg, name))


class Sample:

    def __init__(self):
        self.message = "Hi"

    def msg(self, name):
        print('{}, {}'.format(self.message, name))


if __name__ == '__main__':
    print("something")