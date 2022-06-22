from django.db import models
#from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class test(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    year = models.IntegerField()
   

    def __str__(self):
        return self.name
      
  
