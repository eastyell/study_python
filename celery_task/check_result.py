from celery.result import AsyncResult
from celery_task.celery import app

# 查看结果，根据提交任务返回的字符串去查询
async_result = AsyncResult(id='706ec412-1663-42a0-8f93-68df31807a99',app=app)

if async_result.successful():
    result=async_result.get()
    print("result",result)
elif async_result.failed():
    print("执行失败")
elif async_result.status=='PENDING':
    print("任务等待中被执行")
elif async_result.status == 'RETRY':
    print("任务异常后正在重试")
elif async_result.status == 'STARTED':
    print("任务已经开始被执行")
