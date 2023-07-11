from rest_framework import serializers
from .models import TemperatureData, HumidityData, PictureData


class TemperatureDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=TemperatureData
        fields=('temperature','node_origination', 'date_created','file_type','dataid','pk')

class HumidityDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=HumidityData
        fields=('humidity','node_origination', 'date_created','file_type','dataid','pk')

class PictureDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=PictureData
        fields=('picture','node_origination', 'date_created','file_type','dataid','pk')