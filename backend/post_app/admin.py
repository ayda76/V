from django.contrib import admin
from import_export.admin import ImportExportModelAdmin 
from .resources import *
from .models import *

@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    
    list_display = ['id',]
    list_filter = ('id', )
    
    resource_class  =PostResource
    
    
@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    
    list_display = ['id',]
    list_filter = ('id', )
    
    resource_class  =CommentResource
