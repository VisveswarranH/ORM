# Ex02 Django ORM Web Application
## Date: 4.11.24

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<WhatsApp Image 2024-10-28 at 20.43.38_2d10b7d2.jpg>)



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('cid', 'name', 'age', 'loan', 'years', 'email')  # Customize fields to display in admin list view
admin.site.register(Customer, CustomerAdmin)

models.py

from django.db import models
from django.contrib import admin

class Customer(models.Model):
    cid = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    loan = models.IntegerField()
    years = models.IntegerField()
    email = models.EmailField()

```



## OUTPUT
![alt text](<Screenshot (4).png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
