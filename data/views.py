from rest_framework import generics 
from rest_framework import permissions
from .models import TemperatureData, HumidityData, PictureData
from.serializers import TemperatureDataSerializer, HumidityDataSerializer, PictureDataSerializer
from .permissions import IsSuperuserOrReadOnly
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import JsonResponse
import json 
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.utils.decorators import method_decorator
import os
from django.conf import settings

@csrf_exempt
def post_view(request):###different than the other views
    permission_classes=permissions.AllowAny
    if request.method=='POST':
        data = json.loads(request.body)
        for item in data:
            temperature=item.get('temperature')
            node_origination=item.get('node_origination')
            date_created=item.get('date_created')
            file_type=item.get('file_type')
            dataid=item.get('dataid')

            obj=TemperatureData(temperature=temperature, node_origination=node_origination, date_created=date_created, file_type=file_type, dataid=dataid)

            obj.save()

        return JsonResponse({'message':'Your data has been updated'})
    
    elif request.method == 'GET':
        return JsonResponse({'message': 'This is a GET request'})
 

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]


    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request=request, username=username, password=password)

        try:
            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'User is authenticated'})
            else:
                return JsonResponse({'message': 'Either password or username is invalid, try again'}, status=400)
        except:
            return JsonResponse({'message': 'Something went wrong when authenticating'})



class LogoutView(APIView):
     permission_classes = [permissions.AllowAny]
     def post(self, request):
          
          try:
               refresh_token = request.data["refresh_token"]
               token = RefreshToken(refresh_token)
               token.blacklist()
               return Response(status=status.HTTP_205_RESET_CONTENT)
          except Exception as e:
               return Response(status=status.HTTP_400_BAD_REQUEST)


class CheckAuthenticationView(APIView):
    def get(self, request, format=None):
        isAuthenticated=User.is_authenticated

        if isAuthenticated: 
            return Response({'is Authenticated':'success'})
        else: 
            return Response({'is Authenticated':'error'})


class ListData(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        datatype = self.request.GET.get('datatype')
        print(datatype)
        if datatype=='temperature':
            return TemperatureDataSerializer
        elif datatype=='humidity': 
            return HumidityDataSerializer
        else:  
            return PictureDataSerializer
    

    def get_queryset(self):
        datatype = self.request.GET.get('datatype')
        queryset = None

        if datatype=='temperature':
            queryset= TemperatureData.objects.all()
        elif datatype=='humidity': 
            queryset= HumidityData.objects.all()
        else:  
            queryset= PictureData.objects.all()
    
        dataid = self.request.GET.get('dataid')
        nodenumber = self.request.GET.get('nodenumber')
        daterange = self.request.GET.get('daterange')
    
        if dataid:
            queryset = queryset.filter(dataid=dataid)

        if nodenumber:
            queryset = queryset.filter(node_origination=nodenumber)

        if daterange:
            queryset = queryset.filter(date_created=daterange)


        return queryset
    

class DeleteData(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        datatype = self.request.GET.get('type')
        queryset = None

        if datatype=='temperature':
            print('here')
            queryset= TemperatureData.objects.all()
        elif datatype=='humidity': 
            queryset= HumidityData.objects.all()
        else:  
            queryset= PictureData.objects.all()
        return queryset
    
    lookup_field='pk'

    def perform_destroy(self, instance):
        datatype = self.request.GET.get('type')

        if datatype == 'picture':
            file_path = os.path.join(settings.MEDIA_ROOT, instance.picture.name)

            if os.path.exists(file_path):
                os.remove(file_path)

        super().perform_destroy(instance)

class TemperatureDetailData(generics.RetrieveAPIView): #to view the detailed data, will be used after searching to see all the information of a certain picture 
    permission_classes = [permissions.AllowAny]

    serializer_class = TemperatureDataSerializer
    queryset=TemperatureData.objects.all()
    lookup_field='pk'

class HumidityDetailData(generics.RetrieveAPIView): #to view the detailed data, will be used after searching to see all the information of a certain picture 
    permission_classes = [permissions.AllowAny]

    serializer_class = HumidityDataSerializer
    queryset=HumidityData.objects.all()
    lookup_field='pk'

class PictureDetailData(generics.RetrieveAPIView): #to view the detailed data, will be used after searching to see all the information of a certain picture 
    permission_classes = [permissions.AllowAny]

    serializer_class = PictureDataSerializer
    queryset=PictureData.objects.all()
    lookup_field='pk'
 
