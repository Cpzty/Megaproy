# Generated by Django 2.2.13 on 2020-06-26 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retos', '0006_auto_20200614_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='emocion_final',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='emocion_inicial',
            field=models.CharField(default='', max_length=50),
        ),
    ]