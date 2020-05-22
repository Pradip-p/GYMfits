# Generated by Django 2.1.5 on 2020-05-21 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GYM', '0007_userschedule_gym'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userschedule',
            name='gym',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.GymInfromation'),
        ),
        migrations.AlterField(
            model_name='userschedule',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GYM.Schedule'),
        ),
        migrations.AlterField(
            model_name='userschedule',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]