from django.contrib import admin
from . models import *
# Register your models here.

class Stonemanager(admin.ModelAdmin):
    list_display=['name','size','price','quantity']
    search_fields=['name']

admin.site.register(Stone,Stonemanager)