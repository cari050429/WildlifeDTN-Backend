# Generated by Django 4.2.2 on 2023-07-13 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_alter_picturedata_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picturedata',
            name='picture',
            field=models.BinaryField(null=True),
        ),
    ]
