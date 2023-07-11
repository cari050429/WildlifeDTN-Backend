from django.db import models


class TemperatureData(models.Model):# model will save the data into the database
    temperature = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    node_origination = models.CharField(max_length=255,null=True)
    date_created = models.DateTimeField(null=True)
    file_type = models.CharField(max_length=50,null=True)
    dataid=models.IntegerField(null=True)

    def __str__(self):
        return f"Data ID: {self.pk}"
    
class HumidityData(models.Model):# model will save the data into the database
    humidity = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    node_origination = models.CharField(max_length=255,null=True)
    date_created = models.DateTimeField(null=True)
    file_type = models.CharField(max_length=50,null=True)
    dataid=models.IntegerField(null=True)

    def __str__(self):
        return f"Data ID: {self.pk}"
    
class PictureData(models.Model):# model will save the data into the database
    picture = models.ImageField()
    node_origination = models.CharField(max_length=255,null=True)
    date_created = models.DateTimeField(null=True)
    file_type = models.CharField(max_length=50,null=True)
    dataid=models.IntegerField(null=True)

    def __str__(self):
        return f"Data ID: {self.pk}"
