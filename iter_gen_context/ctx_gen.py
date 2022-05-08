from contextlib import contextmanager


@contextmanager
def open_file(name):
    f = open(name, 'w')
    try:
        yield f
    finally:
        f.close()


with open_file('some_file') as f:
    f.write('hola!')


@contextmanager
def writable_file(file_path):
    file = open(file_path, mode="w")
    try:
        yield file
    finally:
        file.close()


with writable_file("hello.txt") as file:
    file.write("Hello, World!")


import time


@contextmanager
def runtime(description):
    print(description)
    start_time = time()
    try:
        yield
    finally:
        end_time = time()
        run_time = end_time - start_time
        print(f"The function took {run_time} seconds to run.")

