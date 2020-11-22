# Generated by Django 2.2.13 on 2020-11-22 22:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('retos', '0005_auto_20201109_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuestionario_autoestima',
            name='p1',
            field=models.CharField(default='Siento que soy una persona digna de aprecio, al menos en igual  medida que los demás', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_autoestima',
            name='p10',
            field=models.CharField(default='A veces pienso que no sirvo para nada', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_autoestima',
            name='p2',
            field=models.CharField(default='Me inclino a pensar que, en conjunto, soy un fracasado', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_autoestima',
            name='p3',
            field=models.CharField(default='Creo que tengo varias cualidades buenas', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_autoestima',
            name='p4',
            field=models.CharField(default='Puedo hacer las cosas tan bien como la mayoría de la gente', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_autoestima',
            name='p5',
            field=models.CharField(default='Creo que no tengo muchos motivos para sentirme orgulloso de mí', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_autoestima',
            name='p6',
            field=models.CharField(default='Tengo una actitud positiva hacia mí mismo', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_autoestima',
            name='p7',
            field=models.CharField(default='En general, estoy satisfecho conmigo mismo', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_autoestima',
            name='p8',
            field=models.CharField(default='Desearía valorarme más a mí mismo', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_autoestima',
            name='p9',
            field=models.CharField(default='A veces me siento verdaderamente inútil', max_length=150),
        ),
        migrations.CreateModel(
            name='Cuestionario_no_realizado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r1', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('r2', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('r3', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('r4', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('r5', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('r6', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('r7', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('r8', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('r9', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('r10', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('r11', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('r12', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
