# Generated by Django 4.2.2 on 2023-07-13 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_alter_temperaturedata_date_difference'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperaturedata',
            name='time_difference',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='temperaturedata',
            name='date_difference',
            field=models.IntegerField(null=True),
        ),
    ]
