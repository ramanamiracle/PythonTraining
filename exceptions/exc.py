class MyCustomError(Exception):
    """My custom exception"""

    def __init__(self, msg, code):
        """Constructor"""
        self.msg = msg
        self.code = code

    def __str__(self):
        return '{}:{}'.format(self.msg, self.code)


def get_item(seq, index):
    """Return the indexed item of the given sequences."""
    try:
        if index >= len(seq):
            raise MyCustomError("You are Heck", "1000")

        result = seq[index]  # may raise IndexError
        print('try succeed')
    except (IndexError, TypeError) as ie:
        print(ie)
        result = 0
        print('Index out of range')
    except Exception as exc:
        result = 0
        print(exc.msg)
        print(exc.code)
        import sys
        sys.exit(exc.code)
    else:  # run if no exception raised
        print('no exception raised')
    # finally:  # always run regardless of whether exception is raised
    #     print('run finally')

    # Continue into the next statement after try-except-finally instead of abruptly terminated.
    print('continue after try-except')
    return result


# print(get_item([0, 1, 2, 3], 1))  # Index within the range
# print('-----------')
print(get_item([0, 1, 2, 3], 4))  # Index out of range
