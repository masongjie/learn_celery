from celery import Celery

app = Celery("tasks", broker="amqp://msj:123456@106.12.72.253:5672")


@app.task()
def add(x, y):
    return x + y



