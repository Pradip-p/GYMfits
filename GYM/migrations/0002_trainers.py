# Generated by Django 3.0.5 on 2020-05-01 16:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GYM', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('age', models.CharField(max_length=20)),
                ('trainer_type', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('about', models.TextField()),
            ],
        ),
    ]
