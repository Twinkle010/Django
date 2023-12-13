from django.shortcuts import render, redirect
from .utils import send_mail_to_client
from .models import *
# Create your views here.

from django.http import HttpResponse
def home(request):
    Car.objects.create(car_name="Nexon")
    return HttpResponse("<h1>Hey I am a Django Server</h1>")


def success_page(request):
    # return HttpResponse("""<h1> This is a success page</h1>
    # <p>Hey this is coming from Django Server </p>
    # <hr>
    # <h3>This is  a html reponse</h3>
    # """)
    peoples = [
        {'name': 'Twinkle', 'age': 10},
        {'name': 'Lily', 'age': 20}
    ]
    send_email(request)
    return render(request, "index.html", context={'peoples': peoples})
    

def send_email(request):
    print("Function Called")
    send_mail_to_client()
    print("email sent")
    return redirect('/')