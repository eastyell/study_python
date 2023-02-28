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

    s = 'sgjqsafgxvyiomsadf'
    s = set(s)
    l = list(s)
    l.sort()
    res = ''.join(l)
    print(res)

    # dict = {'name': 80, 'age': 18, 'city': 78, 'tel': 123}
    # list = sorted(dict.items(), key=lambda i: i[1], reverse=False)
    # print('sorted根据字典建排序：', list)

    a = ['苏州', '中国', '哈哈', '', '日本', '', '英国']
    res = list(map(lambda x: '无数据' if x == '' else x, a))
    print(res)