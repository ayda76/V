from django.db import models
from profile_app.models import Profile
# Create your models here.
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Request(models.Model):

    
    SELECT_STATUS     = (('done','done'),('unRead','unRead') ,('read','read') )
    status           = models.CharField(max_length=55, choices= SELECT_STATUS ,default='unRead' )
    
    sender          = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='request_sender')
    receiver        = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='request_receiver')
    link            = models.CharField(max_length=230,blank=True, null=True)
    title           = models.CharField(max_length=230,blank=True, null=True)
    text            = models.TextField(blank=True, null=True)
    
    content_type    = models.ForeignKey(ContentType,blank = True , null = True , on_delete=models.CASCADE)
    object_id       = models.PositiveIntegerField(blank = True , null = True )
    content_object  = GenericForeignKey("content_type", "object_id")
    
    requestRelated  = models.ForeignKey('self', blank = True , null = True,on_delete=models.CASCADE,related_name='first_requested')
    
    is_accepted     = models.BooleanField(default=False,blank=True, null=True)
    is_denied       = models.BooleanField(default=False,blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)          
    class Meta:
        verbose_name = "Request"
        verbose_name_plural = "Request" 