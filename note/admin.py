from django.contrib import admin
from .models import *
# Register your models

class Notemanager(admin.ModelAdmin):
    list_display=['title','usermessage_id']
    search_fields=['title']

admin.site.register(Note,Notemanager)
