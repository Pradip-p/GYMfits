# Generated by Django 2.1 on 2020-05-09 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GYM', '0009_schedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='time',
            new_name='starttime',
        ),
        migrations.AddField(
            model_name='schedule',
            name='endtime',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]
