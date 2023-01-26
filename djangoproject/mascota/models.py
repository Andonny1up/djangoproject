from django.db import models

# Create your models here.

class Pet(models.Model):
    name = models.TextField(max_length=100)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    recue_date = models.DateField()
    