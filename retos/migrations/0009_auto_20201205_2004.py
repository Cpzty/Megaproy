# Generated by Django 2.2.13 on 2020-12-06 02:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retos', '0008_auto_20201205_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial_emociones',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
