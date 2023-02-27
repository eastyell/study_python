# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from types import MethodType


class Cat(object):
    def __int__(self):
        super().__init__()


def run(self):
    print('cat is running!')


def main():
    cat01 = Cat()
    cat01.run = MethodType(run, cat01)
    cat01.run()


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     main()

import datetime
import threading


def run():
    print(datetime.datetime.now())
    r_t01 = threading.Timer(1, run)
    r_t01.start()


if __name__ == '__main__':
    # t01 = threading.Thread(target=run)
    # t01.start()
    data = {i: i**2 for i in range(1, 9)}
    print(data)