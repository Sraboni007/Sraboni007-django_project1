from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from .manager import CustomManager
# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField("email_address",unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = CustomManager() 
    
    def __str__(self):
        return self.email
    