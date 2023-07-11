# Generated by Django 4.2.2 on 2023-07-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_remove_data_picture_data_dataid_data_temperature_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HumidityData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('node_origination', models.CharField(max_length=255, null=True)),
                ('date_created', models.DateTimeField(null=True)),
                ('file_type', models.CharField(max_length=50, null=True)),
                ('dataid', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PictureData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
                ('node_origination', models.CharField(max_length=255, null=True)),
                ('date_created', models.DateTimeField(null=True)),
                ('file_type', models.CharField(max_length=50, null=True)),
                ('dataid', models.IntegerField(null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Data',
            new_name='TemperatureData',
        ),
    ]
