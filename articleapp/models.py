from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4

class Signup(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_uuid = models.CharField(max_length = 300)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique = True)
    email = models.EmailField(unique = True, default = None)
    password = models.CharField(max_length = 200)
    date_of_birth = models.DateField(null=True, blank=True, default = None)
    
    def __str__(self):
        return self.user.username
