from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# abstractbaseuser provides all properties of base user and can add additional
# abstract user doesnt give all properties of base user 

class CustomUser(AbstractUser):
    
    username  = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50)
    user_profile_image = models.ImageField(upload_to="profile")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []