from import_export import resources
from .models import *

class PostResource(resources.ModelResource):
     class Meta:
          model = Post
 
class CommentResource(resources.ModelResource):
     class Meta:
          model = Comment        
          
          
