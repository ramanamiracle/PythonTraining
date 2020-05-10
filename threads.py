import time
from threading import Thread


def task1():
	while True:
		print('Something from task1')
		time.sleep(10)


def task2():
	while True:
		print('Something from task2')
		time.sleep(5)


if __name__ == '__main__':
	thread1 = Thread(target=task1)
	thread2 = Thread(target=task2)
	thread1.start()
	thread2.start()
	while True:
		time.sleep(1)
