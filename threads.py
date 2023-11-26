# 线程加锁
import time
import threading

number = 0
lock = threading.Lock()             # 实例化一个锁


class MyThread(threading.Thread):

    def __init__(self, n):
        self.n = n
        super().__init__()

    def run(self) -> None:
        print('当前线程:', threading.current_thread().name)
        global number
        for i in range(1000000):
            with lock:      # with上下文管理器
                number += 1


for i in range(1, 3):
    t = MyThread(i)
    t.start()

# 给5秒钟让两个子线程执行完毕
time.sleep(5)
# 确保两个子线程执行完毕
print("活跃的线程个数：", threading.active_count())
# 输出最终数值
print("number: ", number)


# 何使用“锁”来保护对银行账户的操作
from time import sleep
from threading import Thread, Lock

class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()

'''
join()会使主线程进入等待状态（阻塞），直到调用join()方法的子线程运行结束。
同时你也可以通过设置timeout参数来设定等待的时间
'''
import time
import threading


class MyThread(threading.Thread):

    def __init__(self, n):
        self.n = n
        super().__init__()

    def run(self) -> None:
        while True:
            _count = threading.active_count()
            print(f"线程-{self.n}", f"当前活跃的线程个数：{_count}")
            time.sleep(self.n)


for i in range(1, 3):
    t = MyThread(i)
    t.start()
    t.join(3)  # 前三秒只有线程1在执行


# 线程中控制线程  线程间通信
'''
Event类会在全局定义一个Flag，当Flag=False时，调用wait()方法会阻塞所有线程；
而当Flag=True时，调用wait()方法不再阻塞。形象的比喻就是“红绿灯”：在红灯时阻塞所有线程，
而在绿灯时又会一次性放行所有排队中的线程。Event类有四个方法：
set()：将Flag设置为True
wait()：等待
clear()：将Flag设置为False
is_set()：返回bool值，判断Flag是否为True
Event的一个好处是：可以实现线程间通信，通过一个线程去控制另一个线程。
'''
import time
import threading

event = threading.Event()
event.set()  # 设定Flag = True


class MyThread(threading.Thread):

    def __init__(self, n):
        self.n = n
        super().__init__()

    def run(self) -> None:
        if self.n in [3, 4]:
            event.clear()  # 设定Flag = False
            event.wait()  # 线程3和4进入等待
            print('线程3和4进入等待')

        for i in range(2):
            _count = threading.active_count() - 1
            print(f"线程-{self.n}", f"当前活跃的子线程个数：{_count}")
            time.sleep(2)
            if self.n == 2 and i == 1:
                # 通过线程2来控制线程3和4
                event.set()
                print('通过线程2来控制线程3和4')


for i in range(1, 5):
    t = MyThread(i)
    t.start()


# 通过event控制线程
class MyThread(threading.Thread):
    def __init__(self, event):
        super().__init__()
        self.event = event

    def run(self):
        print('线程{}已经初始化，随时准备启动...'.format(self.name))
        self.event.wait()
        print('{}开始执行...'.format(self.name))


if __name__ == '__main__':
   event = threading.Event()
   threads = []
   [threads.append(MyThread(event)) for i in range(11)]
   event.clear()
   [t.start() for t in threads]
   print('等待5秒启动线程')
   time.sleep(5)
   event.set() # 恢复启动线程
   [t.join() for t in threads]


# 通过Condition对话方式通知线程
cond = threading.Condition()

class father(threading.Thread):
    def __init__(self, cond, name):
        threading.Thread.__init__(self, name=name)
        self.cond = cond

    def run(self):
        self.cond.acquire()   # 获取锁
        print(self.getName() + ': 作业做完了？')
        self.cond.notify()
        self.cond.wait()

        print(self.getName() + ': 多久做完？')
        self.cond.notify()
        self.cond.release()  # 释放锁

class son(threading.Thread):
    def __init__(self, cond, name):
        threading.Thread.__init__(self, name=name)
        self.cond = cond

    def run(self):
        self.cond.acquire()  # 获取锁
        self.cond.wait()

        print(self.getName() + ': 还没做完')
        self.cond.notify()
        self.cond.wait()

        print(self.getName() + ': 还有半个小时')
        # self.cond.notify()
        self.cond.release()  # 释放锁


if __name__ == '__main__':
   ljh = father(cond, '爸爸')
   lyc = son(cond, '儿子')
   lyc.start()
   ljh.start()

# Queue 消息队列实现不同线程间通信
from queue import Queue
import threading
import time


# 生产者消费者模式
def product(q):
    kind = ('猪肉', '牛肉', '白菜')
    for i in range(3):
        print(threading.current_thread().name, '开始生成包子...')
        time.sleep(1)
        q.put(kind[i % 3])
        print(threading.current_thread().name, '包子做完了...')


def comsumer(q):
    while True:
        print(threading.current_thread().name, '开始吃包子')
        time.sleep(1)
        t = q.get()
        print('消费者吃了一个{}包子'.format(t))


if __name__ == '__main__':
    q = Queue(maxsize=1)  # 队列中只存放一个任务
    # 创建生产者线程
    for i in range(3):
        threading.Thread(target=product, args=(q,)).start()
        # threading.Thread(target=product, args=(q,)).start()
    # 创建消费者线程
    for i in range(1):
       threading.Thread(target=comsumer, args=(q,)).start()


# 创建全局ThreadLocal对象
local_school = threading.local()


class Student():
    def __init__(self, name):
        self.name = name


def process_student(name):
    std = Student(name)
    local_school.student = std   # 写操作
    do_task_1()
    do_task_2()


def do_task_1():
    std = local_school.student  # 读操作
    print("do_task_1", std.name)


def do_task_2():
    std = local_school.student   # 读操作
    print("do_task_2", std.name)


if __name__ == '__main__':
    t1 = threading.Thread(target=process_student, args=("Curry",))
    t2 = threading.Thread(target=process_student, args=("大雄",))
    t1.start()
    t2.start()


# 线程池
from concurrent.futures import ThreadPoolExecutor, \
    as_completed, wait, ALL_COMPLETED, FIRST_COMPLETED
import time

executor = ThreadPoolExecutor(max_workers=5)  # 最大线程池数


def get_html(times):
    start = time.time()
    time.sleep(times)
    print('获取网页信息{}完毕'.format(times))
    print('任务{}消耗时间为：'.format(times), time.time() - start)
    return times


tasks = [executor.submit(get_html, i) for i in range(1, 11)]
# 判断线程是否执行完成
time.sleep(2)
if tasks[1].done():
    print('任务1被执行完成')
else:
    print('任务1未被执行完成')
# if tasks[9].cancel():  # 还未被放入线程池中的可取消
#     print('任务9被取消')

# 获取任务的返回值
# as_completed 返回值的顺序根据执行速度和时间
# map 返回值的顺序根据map的顺序
for item in as_completed(tasks):  # as_completed 一个生成器
    data = item.result()
    print('主线程中获取任务的返回值是{}'.format(data))

for data in executor.map(get_html, [4, 2, 3]):
    print('主线程中获取任务的返回值是{}'.format(data))

# wait 让主线程阻塞，直到指定的条件成立
# ALL_COMPLETED 所有任务完成
# FIRST_COMPLETED 只要一个任务完成即可
wait(tasks, return_when=ALL_COMPLETED)
print('代码执行完毕!')


# 线程同步信号量 控制线程执行的数量
import threading, time


class HtmlSPider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self) -> None:
        time.sleep(2)
        print('获取网页内容:', self.url)
        self.sem.release()  # 释放锁


class UrlProduct(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self) -> None:
        for i in range(20):
            self.sem.acquire()  # 获取线程锁
            html_thread = HtmlSPider('http://www.baidu.com/{}'.format(i), self.sem)
            html_thread.start()


if __name__ == '__main__':
    sem = threading.Semaphore(value=3)  # 控制线程每次执行3个子线程
    url_product = UrlProduct(sem)
    url_product.start()





