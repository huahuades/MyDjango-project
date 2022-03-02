from django.contrib import admin
from . models import *
# Register your models here.

class Brickmanager(admin.ModelAdmin):
    list_display=['name','size','price','quantity']
    list_filter=['quantity']
    search_fields=['name']
    list_editable=['price']
admin.site.register(Brick,Brickmanager)