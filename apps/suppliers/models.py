from django.db import models

# Create your models here.
class Proveedor(models.Model):
    first_name = models.CharField(max_length=150,null=False,blank=False)
    last_name = models.CharField(max_length=150,null=True,blank=True)
    company = models.CharField(max_length=150,null=True,blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True,blank=True)

    def __str__(self):
        return self.first_name