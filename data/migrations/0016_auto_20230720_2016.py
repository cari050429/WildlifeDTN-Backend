# Generated by Django 3.2.7 on 2023-07-20 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0015_alter_picturedata_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='humiditydata',
            name='date_created_seconds',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='picturedata',
            name='date_created_seconds',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='temperaturedata',
            name='date_created_seconds',
            field=models.IntegerField(null=True),
        ),
    ]