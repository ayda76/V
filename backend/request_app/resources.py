from import_export import resources
from .models import *

class RequestResource(resources.ModelResource):
     class Meta:
          model = Request