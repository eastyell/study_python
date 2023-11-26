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


# Press the green button in the gutt.er to run the script.
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


# 类装饰器
class MyDecorator(object):
    def __init__(self, func):
        self.__func = func

    # 实现__call__方法，让对象变成可调用的对象，
    # 可调用的对象能够像函数一样被使用。
    def __call__(self, *args, **kwargs):
        # 对已有参数进行封装
        print('--正在进行类装饰-----')
        self.__func(*args)


@MyDecorator
def show(name):
    print("hello:", name)


# 指向MyDecorator类创建实例对象--> show()==> 对象（）
show('Leo')

# 闭包
def func_out(num1):
    def func_inner(num2):
        result = num1 + num2
        print('结果是：', result)
    return func_inner


func_out(10)(10)

# 三元函数
# num = input('please input a num:')
num = 216
result = '偶数' if int(num) % 2 == 0 else '奇数'
print('7，这个数字', num, '是：', result)

num = list(map(lambda x: '偶数' if int(x) % 2 == 0 else '奇数', range(1, 11)))
# dict_value = dict((i, '偶数' if i % 2 == 0 else '奇数') for i in range(10))
print(num)

# 随机函数
import random
import string

str1 = string.ascii_letters  # 英文
str2 = string.digits  # 数字
str3 = str1 + str2
print('8，随机英文和数字：', str3)

str_a = ''
for i in range(6):
    str_a += random.choice(str3)

print('9.随机生成6位字符：', str_a)


# 从序列中随机选择的k个元素，并且这些元素是不重复的。
b = random.sample(str3, 20)
str_b = ''.join(b)
print('随机生成6位字符：', str_b)

# 从序列中随机选择的k个元素,某些元素可能会被选择多次。
b = random.choices(str3, k=20)
str_b = ''.join(b)
print('随机生成20位字符：', str_b)

