from django.contrib.auth.models import User
from django.db import models

class account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=128)

