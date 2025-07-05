from rest_framework import serializers
from django.conf import settings
from django.contrib.auth.models import User

from rest_framework import serializers
from request_app.models import * 
from profile_app.api.serializers import ProfileSerializer


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Request
        fields='__all__'
        
class RequestWithRelatedSerializer(serializers.ModelSerializer):
    sender=ProfileSerializer(required=True)
    receiver=ProfileSerializer(required=True)
    requestRelated=RequestSerializer(required=False)
    class Meta:
        model=Request
        fields='__all__'       
        
class RequestAnswerSerializer(serializers.Serializer):
    request_id=serializers.IntegerField()
    answer=serializers.CharField()