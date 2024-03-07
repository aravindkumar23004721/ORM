# Ex02 Django ORM Web Application
## Date: 28.02.2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

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

'''
admin.py 

from django.contrib import admin
from .models import book_details,book_detailsAdmin
admin.site.register(book_details,book_detailsAdmin)

model.py

from django.db import models
from django.contrib import admin
class book_details(models.Model):
    no=models.IntegerField(primary_key=True);
    name=models.CharField(max_length=66);
    author=models.CharField(max_length=66);
    year=models.IntegerField();
    price=models.IntegerField();

class book_detailsAdmin(admin.ModelAdmin):
    list_diaplay=("no","name","author","year","price");
'''
# Create your models here.

# Register your models here.


## OUTPUT

![alt text](<Screenshot 2024-03-07 201014.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
