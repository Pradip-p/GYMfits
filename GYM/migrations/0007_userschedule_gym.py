# Generated by Django 2.1.5 on 2020-05-21 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
        ('GYM', '0006_gymcontent_gym'),
    ]

    operations = [
        migrations.AddField(
            model_name='userschedule',
            name='gym',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.GymInfromation'),
        ),
    ]
