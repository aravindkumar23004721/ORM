<<<<<<< HEAD
# Ex02 Django ORM Web Application
## Date: 28.02.2024
=======
# Django ORM Web Application
>>>>>>> 06d3e8697c6ae1b73781c76a7c5025777b1fdb80

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

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
## STEP 5:
End the Program
## PROGRAM
## code to edit in 'models.py'
```

<<<<<<< HEAD
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

=======
from django.db import models
from django.contrib import admin


# Create your models here.
class Student (models.Model):
    referencenumber=models.CharField(primary_key=True,max_length=20,help_text="reference number")
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    number=models.IntegerField()

class StudentAdmin(admin.ModelAdmin):
    list_display=('referencenumber','name','age','email','number')



```
## codes to edit in 'admin.py'
```
from django.contrib import admin
from .models import Student,StudentAdmin


# Register your models here.
admin.site.register(Student,StudentAdmin)


```
>>>>>>> 06d3e8697c6ae1b73781c76a7c5025777b1fdb80

## OUTPUT
![adminoutput](https://github.com/Kishorerz/django_orm_app/assets/144451216/b15647e6-b985-463d-b534-7e5895831124)


<<<<<<< HEAD
![alt text](<Screenshot 2024-03-07 201014.png>)
=======
>>>>>>> 06d3e8697c6ae1b73781c76a7c5025777b1fdb80


## RESULT
The student table is created successfully and the program successfully Executed.
