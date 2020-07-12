import sys


def one():
    print('One')


def two():
    print('two')


print(sys.argv)

try:
    if sys.argv[1] == 'one':
        one()
    else:
        two()
except Exception as exc:
    print(exc)
    print('Please pass arg')

