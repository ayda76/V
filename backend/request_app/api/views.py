from rest_framework import generics, viewsets
from rest_framework.decorators import api_view ,permission_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView , CreateAPIView, UpdateAPIView,DestroyAPIView
from rest_framework.exceptions import ValidationError

from profile_app.api.serializers import *
from profile_app.models import *
from request_app.api.serializers import *
from request_app.models import *


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    my_tags = ["Request"]

class AnswerRequestsView(CreateAPIView):
    my_tags=['Request']
    serializer_class=RequestAnswerSerializer
    def post(self,request):
        profile_selected=Profile.get_user_jwt(self,request=self.request)
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            request_id=serializer.validated_data['request_id']
            answer=serializer.validated_data['answer']
        
        try:
            requestSelected=Request.objects.filter(id=request_id,receiver=profile_selected)
            requestSelected=requestSelected[0]
            if answer=='accept':
                requestSelected.is_accepted=True
                requestSelected.save()
                requestSelected.receiver.followers.add(requestSelected.sender)
                requestSelected.receiver.save()
            else:
                requestSelected.is_denied=True
                requestSelected.save()
                
            requestSelected.status='done'
            requestSelected.save()
            serialized_request=RequestWithRelatedSerializer(requestSelected).data
            return Response(serialized_request)    
        except:
            raise ValidationError(detail='something went wrong' ,code = 400)
    
class MyReceivedRequestsView(ListAPIView):
    queryset = Request.objects.all()
    serializer_class=RequestWithRelatedSerializer
    my_tags=['Request']
    def list(self,request):
        profile_selected=Profile.get_user_jwt(self,request=self.request)
        requests_selected=self.queryset.filter(receiver=profile_selected)
        requestList=[]
   
        for request in requests_selected:
        
            request.status='read'
            request.save()
            requestList.append(request)

        serialized_requests=RequestWithRelatedSerializer(requestList, many=True).data
        return Response(serialized_requests)

class MySentRequestsView(ListAPIView):
    queryset = Request.objects.all()
    serializer_class=RequestWithRelatedSerializer
    my_tags=['Request']

    
    def list(self,request):
        try:
            profile_selected=Profile.get_user_jwt(self,request=self.request)        
            requests_selected=Request.objects.filter(sender=profile_selected)
            serialized_requests=RequestWithRelatedSerializer(requests_selected, many=True)
            return Response(serialized_requests.data)
        except:
            return ValidationError(detail='something went wrong' ,code = 400)