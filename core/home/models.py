import email
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    imaage = models.ImageField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)

class Car(models.Model):
    car_name = models.CharField(max_length=10)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name


#Signals
@receiver(post_save, sender = Car) # sender =model name
def call_car_api(sender, instance, **kwargs):
    print("Car created")
    print(sender, instance, kwargs)

# all the logic has to be written in views
# syntax to save objects
# create django shell
# car = Car(car_name="Lily", speed=40) car is the model manager
# car.save()
# or car=Car.objects.create(car_name="Nexon", speed=100)
#car_dict={"car_name":"Alto", "speed":100}
#>>> Car.objects.create(**car_dict)

# to read:
# Car.objects.all() : returns all objects
# Car.objects.all()[0].car_name to get car_name
# get objects of a specific id
# Car.objects.get(id=0) , raises exception if id doesnt exist
# Car.objects.filter(id=10), doesnot raise exception if not exists, returns empty data

#update
#a=Car.objects.get(id=4)
#a.car_name="TestCar"
#a.speed=100
#a.save()

#delete
# Car.objects.all().delete() ;deletes all records
# Car.objects.get(id=3).delete()
# (1, {'home.Car': 1})