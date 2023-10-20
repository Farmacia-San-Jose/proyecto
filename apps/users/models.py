from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    telephone= models.CharField(max_length=20, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if(self.first_name==''):
            return '{}'.format(self.username)
        return '{} {}'.format(self.first_name, self.last_name)
    
    def get_full_name(self):
        if(self.first_name==''):
            return '{}'.format(self.username)
        return '{} {}'.format(self.first_name, self.last_name)