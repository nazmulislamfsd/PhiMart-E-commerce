from django.db import models
from django.contrib.auth.models import AbstractUser
from users.manager import CustomUserManager

# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True) # override field
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email' # Use email instead of username
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    