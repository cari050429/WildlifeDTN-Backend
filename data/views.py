from rest_framework import generics 
from rest_framework import permissions
from .models import TemperatureData, HumidityData, PictureData, Node, Sensor
from.serializers import TemperatureDataSerializer, HumidityDataSerializer, PictureDataSerializer, NodeSerializer, SensorSerializer
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
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.utils.decorators import method_decorator
import os
from django.conf import settings
import datetime
from datetime import datetime
import base64
import io 
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.exceptions import ObjectDoesNotExist

def download(request):
        datatype = self.request.GET.get('datatype')

        if datatype=='temperature':
            queryset= TemperatureData.objects.all()
            serializer = TemperatureDataSerializer(queryset, many=True)
        elif datatype=='humidity': 
            queryset= HumidityData.objects.all()
            serializer = HumidityDataSerializer(queryset, many=True)
        else:  
            queryset= PictureData.objects.all()
            serializer = PictureDataSerializer(queryset, many=True)
    
        dataid = self.request.GET.get('dataid')
        nodenumber = self.request.GET.get('nodenumber')
        daterange = self.request.GET.get('daterange')
    
        if dataid:
            queryset = queryset.filter(dataid=dataid)

        if nodenumber:
            queryset = queryset.filter(node_origination=nodenumber)

        if daterange:
            queryset = queryset.filter(date_created=daterange)


        data = serializer.data
        return JsonResponse(data, safe=False)

@csrf_exempt
def post_node_sensor(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        for item in data:
            node_number = item.get('node_number')
            location = item.get('location')
            sensors = item.get('sensor')


            try:
                node = Node.objects.get(node_number=node_number)
                if node.location != location:
                    # Create a new Node if the location has changed
                    node = Node.objects.create(node_number=node_number, location=location)
            except Node.DoesNotExist:
                # Create a new Node if it doesn't exist
                node = Node.objects.create(node_number=node_number, location=location)

            
            Sensor.objects.update_or_create(
                node=node,
                sensor_name=sensors
            )
            distinct_sensor_count = Sensor.objects.values('sensor_name').distinct().count()
            node.distinct_sensor_count = distinct_sensor_count

            node.save()

        return JsonResponse({'message': 'Tables populated successfully.'})

    # Return an error response for other HTTP methods
    return JsonResponse({'error': 'Invalid request method.'}, status=405)

from datetime import datetime

@csrf_exempt
def post_view(request):###different than the other views
    permission_classes=permissions.AllowAny
    if request.method == 'POST':
        data = json.loads(request.body)
        for item in data:
            if 'temperature' in item:
                temperature = item.get('temperature')
                node_number = item.get('node_origination')
                date_created = datetime.strptime(item.get('date_created'), '%Y-%m-%d %H:%M:%S')
                file_type = item.get('file_type')
                dataid = item.get('dataid')
                date_inputted = datetime.now()
                time_difference = (date_inputted-date_created).total_seconds()
                print(time_difference)

                try:
                    node = Node.objects.get(node_number=node_number)
                except Node.DoesNotExist:
                    # Create a new Node if it doesn't exist
                    node = Node.objects.create(node_number=node_number)

                obj = TemperatureData.objects.create(
                    temperature=temperature,
                    node_origination=node,
                    date_created=date_created,
                    file_type=file_type,
                    dataid=dataid,
                    date_inputted=date_inputted,
                    time_difference=time_difference,
                
                )

            elif 'humidity' in item:
                humidity = item.get('humidity')
                node_number = item.get('node_origination')
                date_created = datetime.strptime(item.get('date_created'), '%Y-%m-%d %H:%M:%S')
                file_type = item.get('file_type')
                dataid = item.get('dataid')
                date_inputted = datetime.now()
                time_difference = (date_inputted-date_created).total_seconds()
                print(time_difference)

                try:
                    node = Node.objects.get(node_number=node_number)
                except Node.DoesNotExist:
                    # Create a new Node if it doesn't exist
                    node = Node.objects.create(node_number=node_number)

                obj = HumidityData.objects.create(
                    humidity=humidity,
                    node_origination=node,
                    date_created=date_created,
                    file_type=file_type,
                    dataid=dataid,
                    date_inputted=date_inputted,
                    time_difference=time_difference,
                )

            elif 'picture' in item:
                picture = item.get('picture')
                picture=picture.strip('""')
                print(picture)
                decoded_image = base64.b64decode(picture)
                node_number = item.get('node_origination')
                date_created = datetime.strptime(item.get('date_created'), '%Y-%m-%d %H:%M:%S')
                file_type = item.get('file_type')
                dataid = item.get('dataid')
                date_inputted = datetime.now()
                time_difference = (date_inputted-date_created).total_seconds()
                print(time_difference)
                image_file = io.BytesIO(decoded_image)

                image_file = InMemoryUploadedFile(
                    image_file,
                     None,
                     f'{dataid}.jpg',
                    'image/jpeg',
                    len(decoded_image),
                    None
    )

                try:
                    node = Node.objects.get(node_number=node_number)
                except Node.DoesNotExist:
                    node = Node.objects.create(node_number=node_number)

                obj = PictureData.objects.create(
                    picture=image_file,
                    node_origination=node,
                    date_created=date_created,
                    file_type=file_type,
                    dataid=dataid,
                    date_inputted=date_inputted,
                    time_difference=time_difference,
                )

        return JsonResponse({'message': 'Your data has been updated'})

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
 
class BlacklistTokenUpdateView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes=()
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)