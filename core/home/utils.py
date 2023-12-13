from home.models import Student
import time

def run_this_function():
    print("Function started")
    time.sleep(1)
    print("Function Executed")

# if we try to directly run this function, will throw an error 
# because we're trying to access django resource
# try to execute the fn in django shell

from django.core.mail import send_mail
from django.conf import settings

def send_mail_to_client():
    subject = "Test Email"
    message = "Just a verification on how django email works!"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["saranyaanagha10@gmail.com"]

    send_mail(subject, message, from_email, recipient_list)