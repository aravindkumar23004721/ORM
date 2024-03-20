# Ex02 Django ORM Web Application
## Date: 28.02.2024

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![WhatsApp Image 2024-03-20 at 09 45 13_ffe691f3](https://github.com/aravindkumar23004721/ORM/assets/148962674/3cfe6daa-36a6-45b1-9c71-9e736520be3f)

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
class book_details(models.Model):
    no=models.IntegerField(primary_key=True);
    name=models.CharField(max_length=66);
    author=models.CharField(max_length=66);
    year=models.IntegerField();
    price=models.IntegerField();
class book_detailsAdmin(admin.ModelAdmin):
    list_diaplay=("no","name","author","year","price");

admin.py
from django.contrib import admin
from .models import book_details,book_detailsAdmin
admin.site.register(book_details,book_detailsAdmin)

```
## OUTPUT
![Screenshot 2024-03-06 095529](https://github.com/aravindkumar23004721/ORM/assets/148962674/bbd96689-00a5-4091-b9e8-2faa64f337b5)
## RESULT
Thus the program for creating a database using ORM hass been executed successfully
