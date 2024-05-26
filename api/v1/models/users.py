from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username = models.CharField(max_length = 50,
                                unique = True)    
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(unique = True,
                              max_length = 100)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


    def __str__(self):
        return self.username
