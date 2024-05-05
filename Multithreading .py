import threading

import time


def quantity():
    for i in range(1, 21):
        print(f' quantity => {i + i}')
        time.sleep(2)


def duplicate():
    for x in range(1, 22):
        print(f'duplicate => {x * x}')
        time.sleep(1)


# thread1 = threading.Thread(target=quantity)
# thread2 = threading.Thread(target=duplicate)
# start = time.time()
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()


def func1():
    for i in range(1, 11):
        print('Hello world')
        time.sleep(1)


def func2():
    for i in range(1, 11):
        print('Hi Guys')
        time.sleep(1)


#
# thread3 = threading.Thread(target=func1)
# thread4 = threading.Thread(target=func2)
#
# start = time.time()
# thread3.start()
# thread4.start()
#
# thread3.join()
# thread4.join()


def func(name: str):
    for i in range(1, 20):
        print(f'hi => {name}')
        time.sleep(2)


def func3(n: int):
    for i in range(1, 21):
        print(f'number => {n * n}')
        time.sleep(3)


thread5 = threading.Thread(target=func, args=('John',))
thread6 = threading.Thread(target=func3, args=(4,))

start_time3 = time.time()

thread5.start()
thread6.start()

thread5.join()
thread6.join()
