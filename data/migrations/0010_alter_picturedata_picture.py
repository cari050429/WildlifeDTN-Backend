# Generated by Django 4.2.2 on 2023-07-13 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_alter_picturedata_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picturedata',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]