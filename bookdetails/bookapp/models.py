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
# Create your models here.
