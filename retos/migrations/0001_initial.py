# Generated by Django 2.2.13 on 2020-08-15 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuestionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('questions_count', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=70)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField()),
                ('roll_out', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CuestionarioRespondido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answers', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retos.Cuestionario')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=1000)),
                ('order', models.IntegerField(default=0)),
                ('cuestionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retos.Cuestionario')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('is_correct', models.BooleanField(default=False)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retos.Pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Reto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Reto_finalizado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finalizado', models.BooleanField(default=False)),
                ('reto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retos.Reto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta_final',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retos.Pregunta')),
                ('respondido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retos.CuestionarioRespondido')),
                ('respuesta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='retos.Respuesta')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('racha', models.IntegerField(default=0)),
                ('alegre', models.IntegerField(default=0)),
                ('caraX', models.IntegerField(default=0)),
                ('triste', models.IntegerField(default=0)),
                ('enojado', models.IntegerField(default=0)),
                ('emocion_inicial', models.CharField(default='', max_length=50)),
                ('emocion_final', models.CharField(default='', max_length=50)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
