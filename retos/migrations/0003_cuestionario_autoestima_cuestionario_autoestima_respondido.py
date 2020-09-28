# Generated by Django 2.2.13 on 2020-09-28 02:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('retos', '0002_auto_20200925_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuestionario_autoestima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1', models.CharField(default='I feel that I am a person of worth, at least on an equal plane with others', max_length=150)),
                ('p2', models.CharField(default='I feel that I have a number of good qualities', max_length=150)),
                ('p3', models.CharField(default='All in all, I am inclined to feel that I am a failure (R)', max_length=150)),
                ('p4', models.CharField(default='I am able to do things as well as most people', max_length=150)),
                ('p5', models.CharField(default='I feel I do not have much to be proud of (R)', max_length=150)),
                ('p6', models.CharField(default='I take a positive attitude toward myself', max_length=150)),
                ('p7', models.CharField(default='On the whole, I am satisfied with myself', max_length=150)),
                ('p8', models.CharField(default='I wish I could have more respect for myself (R)', max_length=150)),
                ('p9', models.CharField(default='I certainly feel useless at times (R)', max_length=150)),
                ('p10', models.CharField(default='At times I think that I am no good at all (R)', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Cuestionario_autoestima_respondido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r1', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)])),
                ('r2', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)])),
                ('r3', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)])),
                ('r4', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)])),
                ('r5', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)])),
                ('r6', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)])),
                ('r7', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)])),
                ('r8', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)])),
                ('r9', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)])),
                ('r10', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)])),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]