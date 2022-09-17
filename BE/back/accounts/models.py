from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import phone_number_validator, zipcode_validator


class User(AbstractUser):

    phone_number = models.CharField(validators = [phone_number_validator], max_length=11, null=True, unique=True)
    addr = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(validators = [zipcode_validator], max_length=5, blank=True)
    nickname = models.CharField(max_length=15, unique=True)
    photo = models.ImageField(upload_to='images/profile/', default='static/profile.jpg')