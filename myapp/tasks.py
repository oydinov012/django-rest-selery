from time import sleep
from celery import shared_task

@shared_task
def my_tast(ism):
    sleep()
    print ('5 sekunt kutdi')
    print(f"yangi task tushdi :", ism)