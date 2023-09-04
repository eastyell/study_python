# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# MethodType 把外部函数(方法)绑定到类或类的实例
from types import MethodType


class Cat(object):
    def __int__(self):
        super().__init__()


def run(self):
    print('1，把外部函数(方法)绑定到类或类的实例', 'cat is running!')


def main():
    cat01 = Cat()
    cat01.run = MethodType(run, cat01)
    cat01.run()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# 每隔一秒启动线程
import datetime
import threading


def run():
    print('2，每隔一秒启动线程:', datetime.datetime.now())
    r_t01 = threading.Timer(1, run)
    r_t01.start()


if __name__ == '__main__':
    t01 = threading.Thread(target=run)
    t01.start()

# 去除重复字符，并排序 升序
# sorted（）是python的内置函数，可以排序的对象有列表、元组、字典、字符串。sorted不改变原对象的值，排序后的对象类型全部为list。
# sort是列表类的方法，只对列表有用。不返回值，直接在列表上操作，会改变原对象的值。
    s = 'sgjqsafgxvyiomsadf'
    print('3，old str:', s)
    # 方法1
    res = set(s)
    res = sorted(res)
    res = ''.join(res)
    print('去除重复字符并排序:', res)
    # 方法2
    s = set(s)
    x = list(s)
    x.sort()
    res = ''.join(x)
    print('去除重复字符并排序:', res)

    # 根据字典建排序
    dict = {'chinese': 80, 'maths': 88, 'english': 78, 'history': 92}
    print('4，old dict:', dict)
    lists = sorted(dict.items(), key=lambda i: i[1], reverse=False)
    print('sorted根据成绩排序：', lists)

    # map函数
    area = ['苏州', '中国', '哈哈', '', '日本', '', '英国']
    print('5，原始数据：', area)
    res = list(map(lambda x: '无数据' if x == '' else x, area))
    print('填充数据：', res)

    #  装饰器
    def my_decorator(func):
        def wrapper(arg):  # 传递参数
            print("Something is happening before the function is called.")
            func(arg)
            print("Something is happening after the function is called.")

        return wrapper
    print('6，装饰器')


    @my_decorator
    def say_whee(arg):
        print(arg + "Whee!")

say_whee('hello ')

# 三元函数
# num = input('please input a num:')
num = 216
result = '偶数' if int(num) % 2 == 0 else '奇数'
print('7，这个数字', num, '是：', result)

# 随机函数
import random
import string

str1 = string.ascii_letters
str2 = string.digits
str3 = str1 + str2
print('8，随机英文和数字：', str3)

str_a = ''
for i in range(6):
    str_a += random.choice(str3)

print('随机生成6位字符：', str_a)

b = random.sample(str3, 6)
str_b = ''.join(b)
print('随机生成6位字符：', str_b)
