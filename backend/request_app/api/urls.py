from rest_framework.routers import DefaultRouter
from request_app.api.views import *
from django.contrib import admin
from django.urls import path , include ,re_path

router = DefaultRouter()


router.register('request',RequestViewSet)

urlpatterns = [

    path("", include(router.urls)),
    path('my_received_requests/',MyReceivedRequestsView.as_view()),
    path('my_sent_requests/',MySentRequestsView.as_view()),
    path('answer_request/',AnswerRequestsView.as_view())

   
]