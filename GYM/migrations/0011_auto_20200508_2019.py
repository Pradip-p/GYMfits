# Generated by Django 2.1 on 2020-05-09 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GYM', '0010_auto_20200508_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='starttime',
            field=models.DateTimeField(),
        ),
    ]
