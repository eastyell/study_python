from celery import Celery
from datetime import timedelta
from celery.schedules import crontab

# include:导入指定的任务模块
# 这一次创建 app，并没有直接指定 broker(消息中间件来接收和发送任务消息) 和 backend(存储结果)。而是在配置文件中。
# demo是实例化产生的celery的名字，因为会存在多个celery
app = Celery(
   'demo',
   # 包含一些2个任务文件，去相应的py文件找任务，对多个任务进行分类
   include=[
      'celery_task.task1',
      'celery_task.task2',
   ]
)

# 通过Celery 实例加载配置模块
app.config_from_object(
   'celery_task.celery_config',
)

# 计划任务
app.conf.beat_schedule = {
   'submit_every_2_seconds': {
      # 计划的任务执行函数
      'task': 'celery_task.task1.send_msg',
      # 每个2秒执行一次
      'schedule': timedelta(seconds=2),
      # 'schedule': crontab(hour=8, day_of_week=1),  # 每周一早八点
      # 传递的任务函数参数
      'args': ('每个2秒执行一次向吕远程发送短信任务',)
   },
   'submit_every_3_seconds': {
      # 计划的任务执行函数
      'task': 'celery_task.task2.send_email',
      # 每个3秒执行一次
      'schedule': timedelta(seconds=3),
      # 传递的任务函数参数
      'args': ('每个3秒执行一次向吕远程发送邮件任务',)
   },
   'submit_in_fix_datetime': {
      'task': 'celery_task.task2.send_email',
      # 比如每年的7月13日10点53分执行
      # 注意：默认使用utc时间，当前的时间中的小时必须要-8个小时才会到点提交
      'schedule': crontab(minute=25, hour=16, day_of_month=19, month_of_year=12),
      'args': ('定时向吕远程发送邮件任务',)
      # '''
      # 如果不想-8，可以先设置时区，再按正常时间设置
      # app.conf.timezone = "Asia/Shanghai"
      # app.conf.enable_utc = True
      # '''
   }

}

# 上面写完后，需要起一个进程，启动计划任务
# celery -A  celery_task beat -l info

# 启动worker：
# celery -A celery_task worker --loglevel=info -P eventlet  -c 10