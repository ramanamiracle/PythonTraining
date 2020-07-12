
def sum1(x, y):
    """ This function is to add two numbers
    x: param1 --> Need to be interger
    y: param2 --> Need to be interger
    return: sum of two parameters x & y"""
    c = x + y
    return c


# f(n)= f(n-1)+f(n-2) and f(1)=f(2)=1
# f(10) --> f(9) + f(8) --> 34 + 21 --> 55
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

# fibon(10)
def fibon(n=10):
    a = 1
    b = 1

    for i in range(n):
        a, b = b, a + b

    return a, b


def mul(a, b):
    return a * b


a, b = fibon(10)

value = mul(a , b)


def fun(name, age, nationality='India'):
    print(name, age, nationality)

# fun('Ramana', 28, nationality='US')


def sum1(*args):
    print(args)
    s = 0
    for i in args:
        s = s + i
    return s


def details(*args, **kwargs):
    print(args)
    print(kwargs)


d = {
    'name': 'Ramana',
    'age': 22,
    'address': 'Hyderabad'
}


def func(a: list, b: list) -> list:
    a += 1
    b += 2
    return a, b


x, y = func('ssss', 10)


