from django.db import models
from profile_app.models import Profile
# Create your models here.


class Post(models.Model):
    Post_Type_Select=(('note','note'),('image','image'),('reels','reels'))
    post_type       =models.CharField(default='note',choices=Post_Type_Select,max_length=30)
    owner           = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='owner_post')
    file_post       = models.FileField(upload_to='media/post/files/% Y/% m/% d/', blank=True, null=True)
    image_post      = models.ImageField(upload_to='media/post/images/% Y/% m/% d/', blank=True, null=True)
    caption         = models.TextField(blank=True, null=True)
    fav_people      = models.ManyToManyField(Profile,related_name='fav_people_post',blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)          
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Post"                     
        
class Comment(models.Model):
    owner         = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='owner_comment')
    postRelated   = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='post_comment')
    image_comment = models.ImageField(upload_to='media/comment/images/% Y/% m/% d/', blank=True, null=True)
    content       = models.TextField(blank=True, null=True)
    fav_people    = models.ManyToManyField(Profile,related_name='fav_people_comment',blank=True)
    replied_on    = models.ForeignKey('self', on_delete=models.CASCADE,related_name='repliedOn_comment',blank=True, null=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)          
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comment"      