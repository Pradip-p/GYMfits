# Generated by Django 2.1 on 2020-05-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gyminfromation',
            name='pic',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
