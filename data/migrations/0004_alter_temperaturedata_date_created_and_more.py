# Generated by Django 4.2.2 on 2023-07-13 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_alter_temperaturedata_date_difference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperaturedata',
            name='date_created',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='temperaturedata',
            name='date_inputted',
            field=models.DateTimeField(null=True),
        ),
    ]
