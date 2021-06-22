from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserPreference(models.Model):
    user = models.OneToOneField(to=User,default="INR - Indian Rupee",on_delete=models.CASCADE)
    currency = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.user) + 's' + 'preferences'