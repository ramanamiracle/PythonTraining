import logging
import concurrent.futures
import time


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    data = [1, 2, 3]

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        try:
            executor.map(thread_function, data)
        except Exception as e:
            print(e)