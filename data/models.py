from django.db import models


class Node(models.Model):
    node_number = models.IntegerField(null=True, unique=True)
    location = models.CharField(max_length=255)
    num_sensors = models.IntegerField(null=True)

    def __str__(self):
        return f"Node {self.node_number}"



class Sensor(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE, to_field='node_number', null=True)
    sensor_name = models.CharField(max_length=255)

    def __str__(self):
        return self.sensor_name

class TemperatureData(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    node_origination = models.ForeignKey(Node, on_delete=models.CASCADE, to_field='node_number', null=True)
    date_created = models.DateTimeField(null=True)
    date_inputted= models.DateTimeField(null=True)
    time_difference = models.IntegerField(null=True)
    file_type = models.CharField(max_length=50, null=True)
    dataid = models.IntegerField(null=True)

    def __str__(self):
        return f"Temperature Data ID: {self.pk}"


class HumidityData(models.Model):
    humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    node_origination = models.ForeignKey(Node, on_delete=models.CASCADE, to_field='node_number', null=True)
    date_created = models.DateTimeField(null=True)
    date_inputted= models.DateTimeField(null=True)
    time_difference = models.IntegerField(null=True)
    file_type = models.CharField(max_length=50, null=True)
    dataid = models.IntegerField(null=True)

    def __str__(self):
        return f"Humidity Data ID: {self.pk}"


class PictureData(models.Model):
    picture = models.ImageField(upload_to='images/', null=True)
    node_origination = models.ForeignKey(Node, on_delete=models.CASCADE, to_field='node_number', null=True)
    date_created = models.DateTimeField(null=True)
    date_inputted= models.DateTimeField(null=True)
    time_difference = models.IntegerField(null=True)
    file_type = models.CharField(max_length=50, null=True)
    dataid = models.IntegerField(null=True)

    def __str__(self):
        return f"Picture Data ID: {self.pk}"