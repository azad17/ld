from celery import shared_task
import time


@shared_task
def send_welcome_email(email):

    time.sleep(5)

    print(f"Email sent to {email}")