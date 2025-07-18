from django.contrib import admin

from import_export.admin import ImportExportModelAdmin 
from .resources import *
from .models import *

@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    
    list_display = ['id',]
    list_filter = ('id', )
    
    resource_class  =ProfileResource
