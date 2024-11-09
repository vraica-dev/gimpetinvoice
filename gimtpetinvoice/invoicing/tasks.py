from celery import shared_task
from provider.models import Provider
import time


@shared_task()
def app1_test():
    try:
        Provider.objects.first().delete()
    except:
        return False
    return True
    