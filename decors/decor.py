def clamp_range(func):  # Take a 1-argument function as argument
    """Decorator to clamp the value of the argument to [0,100]"""
    def _wrapper(x):    # Applicable to functions of 1-argument only
        if x < 0:
            x = 0
        elif x > 100:
            x = 100
        return func(x)  # Run the original 1-argument function with clamped argument
    return _wrapper


@clamp_range # clamp_range(square)
def square(x):
    return x*x


@clamp_range # clamp_range(square)
def triple(x):
    return x*x*x


def clamp_range(func):
    """Decorator to clamp the value of ALL arguments to [0,100]"""
    def _wrapper(*args):
        newargs = []
        for item in enumerate(args):
            if item < 0:
                newargs.append(0)
            elif item > 100:
                newargs.append(100)
            else:
                newargs.append(item)
        return func(*args)  # Run the original function with clamped arguments
    return _wrapper


@clamp_range
def my_add(x, y, z):
    return x + y + z


# =====================================================================

from functools import wraps


def clamp_range(min, max):    # Take the desired arguments instead of func
    """Decorator to clamp the value of ALL arguments to [min,max]"""
    def _decorator(func):     # Take func as argument
        @wraps(func)          # For proper __name__, __doc__
        def _wrapper(*args):  # Decorate the original function here
            newargs = []
            for item in args:
                if item < min:
                    newargs.append(min)
                elif item > max:
                    newargs.append(max)
                else:
                    newargs.append(item)
            return func(*newargs)  # Run the original function with clamped arguments
        return _wrapper
    return _decorator


@clamp_range(1, 10)
def my_add(x, y, z):
    """Clamped Add"""
    return x + y + z

# Same as
# my_add = clamp_range(min, max)(my_add)
# 'clamp_range(min, max)' returns '_decorator(func)'; apply 'my_add' as 'func'

print(my_add(1, 2, 3))     # Output: 6
print(my_add(-1, 5, 109))  # Output: 16 (1+5+10)
print(my_add.__name__)     # Output: add
print(my_add.__doc__)      # Output: Clamped Add
