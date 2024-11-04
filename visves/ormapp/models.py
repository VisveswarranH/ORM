from django.db import models
from django.contrib import admin

class Customer(models.Model):
    cid = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    loan = models.IntegerField()
    years = models.IntegerField()
    email = models.EmailField()
