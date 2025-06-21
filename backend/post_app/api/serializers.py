from rest_framework import serializers
from django.conf import settings
from django.contrib.auth.models import User


from rest_framework import serializers

from post_app.models import * 
from profile_app.api.serializers import ProfileSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'

class PostWithRelatedSerializer(serializers.ModelSerializer):
    owner=ProfileSerializer(required=True)
    fav_people=serializers.SerializerMethodField()
    class Meta:
        model=Post
        fields='__all__'
        
    def get_fav_people(self,obj):
        favPeople=obj.fav_people.all()
        listFav=[]
        for people in favPeople:
            data={'id':people.id,'name':people.firstName,'avatar':people.avatar}
            listFav.append(data)
            
        return listFav
        
class  CommentSerializer(serializers.ModelSerializer):
    class Meta:
        models= Comment
        fields='__all__'                                                           


class  CommentWithRelatedSerializer(serializers.ModelSerializer):
    owner=ProfileSerializer(required=True)
    fav_people_num=serializers.SerializerMethodField()
    replied_comments=serializers.SerializerMethodField()
    class Meta:
        models= Comment
        fields='__all__' 
        
    def get_fav_people_num(self,obj):      
        fav_people=obj.fav_people.all() 
        return len(fav_people)

    def get_replied_comments(self,obj):
        reply_comments=Comment.obiects.filter(replied_on=obj)
        if len(reply_comments)>0:
            return CommentSerializer(reply_comments,many=True).data
        else:
            return 'no reply'                          