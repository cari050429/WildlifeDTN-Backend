# Generated by Django 4.2.2 on 2023-07-13 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_alter_picturedata_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picturedata',
            name='picture',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
