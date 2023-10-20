from django.db import models

# Create your models here.
class Presentacion(models.Model):
    
    presentation_type = models.CharField(max_length=150, null=False,blank=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.presentation_type