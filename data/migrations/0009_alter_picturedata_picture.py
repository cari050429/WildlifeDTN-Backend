# Generated by Django 4.2.2 on 2023-07-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_humiditydata_date_inputted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picturedata',
            name='picture',
            field=models.BinaryField(null=True),
        ),
    ]