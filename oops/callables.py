class MyCallable:

    def __init__(self, value):
        self.value = value

    def __call__(self):
        return 'The value is %s' % self.value

    def __str__(self):
        return f'MyCallable({self.value})'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

    def __enter__(self):
        print('enter')


if __name__ == '__main__':
    # Construct an instance
    obj = MyCallable(88)
    print(obj)
    # Call the instance, invoke __call__()
    print(obj())  # Output: The value is 88
