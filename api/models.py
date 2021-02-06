from django.db import models

# Create your models here.

class Owner(models.Model):
    
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ['name']