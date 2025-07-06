from rest_framework.routers import DefaultRouter

from django.contrib import admin
from django.urls import path , include ,re_path
from post_app.models import *
from post_app.api.views import *
router = DefaultRouter()

router.register("post",PostViewSet)
router.register("comment",CommentViewSet)


urlpatterns = [

    path("", include(router.urls)),
    path('PostsYouSee/', PostsYouSee.as_view()),

    
]
