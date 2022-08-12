from django.db import models
from django.contrib.auth.models import AbstractUser 


class User(AbstractUser):
    photo = models.ImageField(upload_to='profile/', default='profile/default.png', blank=True,null=True)
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

