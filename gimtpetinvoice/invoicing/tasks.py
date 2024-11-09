from base.celery import app
import time


@app.task()
def app1_test():
    print('I am app1_test task!')
    time.sleep(2)