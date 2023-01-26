from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    age = models.IntegerField()
    phone = models.TextField(max_length=12)
    email = models.EmailField()
    address = models.TextField(200)