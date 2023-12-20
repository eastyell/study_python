# celery 分布式的异步任务框架

### celery能做什么？

-异步执行：解决耗时任务，将“耗时操作任务”提交给Celery去异步执行，比如发送短信/邮件、消息推送、音视频处理等。

-延迟执行：解决延迟任务。

-定时执行：解决周期(周期)任务，比如每天数据统计。

### celery架构中的几个主要组件为：

#### 任务模块 Task

包含异步任务和定时任务。其中，异步任务通常在业务逻辑中被触发并发往任务队列，而定时任务由 Celery Beat 进程周期性地将任务发往任务队列。

#### 消息中间件(broker)

Celery本身不提供消息服务，但是可以方便地和第三方提供的消息中间件集成，包括 Redis 等。
 
#### 任务执行单元(worker)

Worker是Celery提供的任务执行的单元，并发运行在分布式的系统节点中(本质：一个work就是一个进程)。
 
#### 任务结果存储（backend）

Task result store用来存储Worker执行的任务的结果，Celery支持以不同方式存储任务的结果，包括 redis 等

### celery简单使用流程：

celery的使用

    -pip3 install celery

    -写一个py文件：celery_task

        -1 指定broker（消息中间件），指定backend（结果存储）

        -2 实例化产生一个Celery对象 app=Celery('名字'，broker，backend)

        -3 加装饰器绑定任务，在函数（add）上加装饰器app.task

        -4 其他程序提交任务,先导入add，add.delay(参，参数)，会将该函数提交到消息中间件，但是并不会执行，有个返回值，直接print会打印出任务的id，以后用id去查询任务是否执行完成

        -5 启动worker去执行任务：

        linux: celery -A celery_task_s1 worker -l info   

        windows下：celery -A celery_task_s1 worker -l info -P eventlet

        注：windows系统需要eventlet支持

        启动 beat 的命令（负责每隔几秒钟，向任务队列中提交任务）
       
        celery beat -A celery_task -l info

        -6 查看结果：根据id去查询

            async = AsyncResult(id="bd600820-9366-4220-a679-3e435ae91e71", app=app)

            if async.successful():

                #取出它return的值

                result = async.get()

                print(result)
### celery的多任务结构
    -项目结构：
        pro_cel
            ├── celery_task# celery相关文件夹
            │   ├── celery.py   # celery连接和配置相关文件,必须叫这个名字
            │   └── tasks1.py    #  所有任务函数
            │   └── tasks2.py    #  所有任务函数
            ├── check_result.py # 检查结果
            └── send_task.py    # 触发任务
    -启动worker，celery_task是包的名字
        celery worker -A celery_task -l info -P eventlet

