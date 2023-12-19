from celery import Celery
from celery.schedules import crontab   # 可以实现复杂的定时任务

broker = 'redis://127.0.0.1:6379'		# 消息中间件
backend = 'redis://127.0.0.1:6379/0'    # backend  存储结果

app = Celery('my_task', broker=broker, backend=backend, broker_connection_retry_on_startup=True)


# 创建定时任务
@app.on_after_configure.connect  # 启动程序连接上celery后自动执行这个函数生成定时任务
def setup_periodic_tasks(sender, **kwargs):   # 第一次参数必须是sender,是定时任务的一个实例
    # 每过 10 s，执行一次 hello 这里的test是我们自定义的函数
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # 每过 30 s，执行一次 world
    sender.add_periodic_task(30.0, test.s('worlds'), expires=10)

    # 每周一七点三十执行一次 Happy Mondays!  更复杂的定时任务
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )


@app.task
def test(arg):
    print('run task:', arg)