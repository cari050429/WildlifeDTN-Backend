from django.contrib import admin
from .models import TemperatureData, HumidityData, PictureData, Node, Sensor

admin.site.register(TemperatureData)
admin.site.register(HumidityData)
admin.site.register(PictureData)
admin.site.register(Node)
admin.site.register(Sensor)

