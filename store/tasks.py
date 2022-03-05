from time import sleep
from celery import shared_task


@shared_task
def notify_customers(message):
    print("Sending 100k Email")
    print(message)
    sleep(10)
    print("Done")
