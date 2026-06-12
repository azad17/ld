from django.core.mail import send_mail
from celery import shared_task

@shared_task
def send_login_email(email):
    send_mail(
        subject = "Login Notofication",
        message="You have logged in",
        from_email="admin@mail.com",
        recipient_list = [email]
    )
    return "Welcome Email sent"
 