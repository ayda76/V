from django.contrib import admin

from import_export.admin import ImportExportModelAdmin 
from .resources import *
from .models import *

@admin.register(Request)
class RequestAdmin(ImportExportModelAdmin):
    
    list_display = ['id',]
    list_filter = ('id', )
    
    resource_class  =RequestResource
