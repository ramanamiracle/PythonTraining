# Python program showing
# use of __call__() method

class MyDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self):
        # We can add some code
        # before function call
        print("before call")
        self.function()
        print("after call")

        # We can also add some code
        # after function call.


# adding class decorator to the function
@MyDecorator
def function():
    print("GeeksforGeeks")


function()