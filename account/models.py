from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class UserAccount(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(blank=True)
    birth_date = models.DateField(blank=True, null=True)
