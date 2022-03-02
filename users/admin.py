from django.contrib import admin
from .models import *
# Register your models here.

class Usermanager(admin.ModelAdmin):
    list_dispaly=['username','password','created_time','updated_time']
    search_fields=['username']

admin.site.register(Usermessage,Usermanager)