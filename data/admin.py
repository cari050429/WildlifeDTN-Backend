from django.contrib import admin
from .models import TemperatureData, HumidityData, PictureData

admin.site.register(TemperatureData)
admin.site.register(HumidityData)
admin.site.register(PictureData)

