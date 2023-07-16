from rest_framework import serializers
from .models import TemperatureData, HumidityData, PictureData, Node, Sensor


class TemperatureDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=TemperatureData
        fields=('temperature','node_origination', 'date_created','date_inputted','time_difference','file_type','dataid','pk')

class HumidityDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=HumidityData
        fields=('humidity','node_origination', 'date_created','date_inputted','time_difference','file_type','dataid','pk')


class PictureDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=PictureData
        fields=('picture','node_origination', 'date_created','date_inputted','time_difference','file_type','dataid','pk')


class NodeSerializer(serializers.ModelSerializer): 
    class Meta: 
        model=Node
        fields=('node_number', 'location', 'num_sensors','pk')

class SensorSerializer(serializers.ModelSerializer): 
    class Meta: 
        model=Node
        fields=('node_id', 'sensor_name', 'pk')