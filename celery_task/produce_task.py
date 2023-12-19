from celery_task.task1 import send_msg
from celery_task.task2 import send_email
from datetime import timedelta
from datetime import datetime

# 延迟执行
ctime = datetime.now()
utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
time_delay = timedelta(seconds=10)
task_time = utc_ctime + time_delay
# 提交任务到消息队列中redis，这里只是将任务提交，并没有执行
# result=send_msg.delay('吕远程')
result = send_msg.apply_async(args=["定时任务-延时10秒"], eta=task_time)
print(result.id)
print(result.get())
result = send_email.apply_async(args=["定时任务-延时10秒"], eta=task_time)
# result=send_email.delay('吕远程')
print(result.id)
print(result.get())

# 定时任务
# 设置任务执行时间2023年12月19日15点30分00秒
v1 = datetime(2023, 12, 19, 15, 30, 00)
# 将v1时间转成utc时间
v2 = datetime.utcfromtimestamp(v1.timestamp())
# 取出要执行任务的时间对象，调用apply_async方法，args是任务函数传的参数，eta是执行的时间
result = send_msg.apply_async(args=["定时任务-2023年12月19日15点30分00秒"], eta=v2)
print(result.id)
print(result.get())