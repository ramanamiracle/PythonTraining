def outer(a):      # Outer function
    print('outer() begins with arg =', a)
    x = 1  # Local variable of outer function

    # Define an inner function
    # Outer has a local variable holding a function object
    def inner(b):
        print(globals())
        print('inner() begins with arg =', b)
        y = 2  # Local variable of the inner function
        print('a = {}, x = {}, y = {}'.format(a, x, y))
        # Have read-access to outer function's attributes
        print('inner() ends')
        return y

    # Call inner function defined earlier
    return inner # y value



# Call outer function, which in turn calls the inner function

f = outer(10)
