# Generated by Django 2.2.13 on 2020-12-13 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retos', '0023_auto_20201211_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='autoestima_finalizado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='comodecirqueno_finalizado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='comunicacion_finalizado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='pec_finalizado',
            field=models.BooleanField(default=False),
        ),
    ]
