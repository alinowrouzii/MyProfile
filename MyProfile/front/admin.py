from django.contrib import admin

from front.models import *
# Register your models here.



@admin.register(StaticData)
class StaticAdmin(admin.ModelAdmin):
    list_display = ['id', 'key', 'value']
    
