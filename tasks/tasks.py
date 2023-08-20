from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_task_assignment_email(recipient_email, task_title):
    subject = 'Task Assigned'
    message = f'You have been assigned a task: {task_title}'
    from_email = 'testsmtp202308@gmail.com'  
    recipient_list = [recipient_email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)