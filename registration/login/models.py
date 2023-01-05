from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Account(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.TextField()
    password = models.TextField()
    
    def __str__(self):
        return self.user.username