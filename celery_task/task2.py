import time
from celery_task.celery import app


# 需要使用一个装饰器，来管理该任务(函数)
# 提交任务到worker
@app.task
def send_email(name):
    print("开始向%s发送邮件任务" % name)
    time.sleep(5)
    return f"发送{name}邮件完成!"
