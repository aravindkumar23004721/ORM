# Ex02 Django ORM Web Application
## Date: 28.02.2024

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![image](https://github.com/Narasimhan05/ORM/assets/132819871/a44fd2ae-237a-4d70-a71b-596c17bc16ee)


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
class Books(models.Model):
    bookid = models.IntegerField(primary_key=True);
    bookname = models.CharField(max_length=50);
    author = models.CharField(max_length=50);
    published = models.DateField();
    price = models.IntegerField();
class BooksAdmin(admin.ModelAdmin):
    list_display = ("bookid","bookname","author","published","price");


admin.py
from django.contrib import admin
from .models import Books,BooksAdmin
admin.site.register(Books,BooksAdmin)

```
## OUTPUT

![Screenshot 2024-03-15 114345](https://github.com/Narasimhan05/ORM/assets/132819871/5881c5cd-f573-4542-b2f7-915447edfb33)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
