# Ex02 Django ORM Web Application
## Date: 28.02.2024

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![WhatsApp Image 2024-03-21 at 21 19 31_48f00566](https://github.com/aravindkumar23004721/ORM/assets/148962674/3491a794-9816-4956-8e23-b1af0d7b201b)


## DESIGN STEPS

### STEP 1:
install myapp using 'python mnage.py startapp [your app name] ' command 

### STEP 2:
first edit 'settings.py' and then edit 'models.py' and then edit 'admin.py' with the appropriate codes .

### STEP 3:
create a user name and password usingfor your django  'python manage.py createsuperuser'
and then run the program using 'python manage.py runserver [your port number]'
### STEP 4:
login with your username and password in django and select student table and then add 10 students detials.
## PROGRAM
```
models.py
from django.db import models
from django.contrib import admin
class libraryBook(models. Model):
    title=models.CharField(max_length=15);
    BookID=models.IntegerField(primary_key=True);
    author=models.CharField(max_length=10);
    publisher=models.CharField(max_length=8);
    price=models.IntegerField();
    pages=models.IntegerField();
class libraryBookAdmin(admin.ModelAdmin):
   list_display=("title","BookID","author","publisher","price","pages");

admin.py
from django.contrib import admin 
from .models import libraryBook,libraryBookAdmin
admin.site.register(libraryBook,libraryBookAdmin)

```
## OUTPUT
![WhatsApp Image 2024-03-21 at 21 19 30_539c244b](https://github.com/aravindkumar23004721/ORM/assets/148962674/4273b6ce-99d5-432e-8dc6-787e97cd9f67)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
