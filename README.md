# Ex02 Django ORM Web Application
## Date: 28.02.2024

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![alt text](<ara .jpg>)

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
models.py

from django.db import models
from django.contrib import admin
class Student_DB(models. Model):
    regno=models.IntegerField(); 
    name=models.CharField(max_length=20); 
    email=models.EmailField(); 
    DoB=models.DateField();
    cgpa=models.IntegerField();
class Student_DBAdmin(admin.ModelAdmin):
    list_display=("regno","name", "email", "DoB","cgpa");

admin.py

from django.contrib import admin
from .models Student_DB,Student_DBAdmin
admin.site.register(Student_DB,Student_DBAdmin)
## OUTPUT
![alt text](<Screenshot 2024-03-07 201014.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
