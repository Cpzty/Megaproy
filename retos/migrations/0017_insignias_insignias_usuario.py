# Generated by Django 2.2.13 on 2020-12-09 05:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('retos', '0016_remove_profile_cantidad_retos_realizados'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insignias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=75)),
                ('descripcion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Insignias_usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registrada', models.DateTimeField(default=datetime.date.today)),
                ('insignia_obtenida', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='retos.Insignias')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
