from django.contrib import admin
from .models import *
# Register your models here.
class Cartmanager(admin.ModelAdmin):
    list_display=['shopname','shopsize','shopprice','shopquantity']
    search_fields=['shopname']

admin.site.register(Cart,Cartmanager)