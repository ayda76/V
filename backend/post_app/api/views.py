from rest_framework import generics, viewsets
from rest_framework.decorators import api_view ,permission_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView , CreateAPIView, UpdateAPIView,DestroyAPIView


from profile_app.api.serializers import *
from profile_app.models import *
from post_app.api.serializers import *
from post_app.models import *


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    my_tags = ["Post"]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    my_tags = ["Post"]

class PostsYouSee(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    my_tags = ["Post"]   
    def list(self,request):
        profile_selected=Profile.get_user_jwt(self,request=self.request)
        followings_selected=Profile.objects.filter(followers__in=[profile_selected])
        all_posts=[]
        for following in followings_selected:
            posts_selected=Post.objects.filter(owner=following.id)
            for post in posts_selected:
                all_posts.append(post)
       
        posts_serialized=PostWithRelatedSerializer(all_posts, many=True)
        return Response(posts_serialized.data)
