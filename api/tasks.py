from celery import shared_task
import time

@shared_task
def send_welcome_email(username):
    print(f"Simulating sending welcome email to {username}")
    time.sleep(5)
    return f"Welcome email sent to {username}"
