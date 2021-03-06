# Generated by Django 2.2.13 on 2020-11-26 01:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('retos', '0006_auto_20201122_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuestionario_comunicacion_efectiva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1', models.CharField(default='Cuando se que tengo derecho a algo (por ejemplo quejarme, expresar mi opinion, etcetera', max_length=150)),
                ('p2', models.CharField(default='En las situaciones en las que no estoy de acuerdo con la opinion del otro…', max_length=150)),
                ('p3', models.CharField(default='Tus intereses chocan con los de tu pareja, amigo… ¿que haces?…', max_length=150)),
                ('p4', models.CharField(default='En el trabajo te piden hacer una tarea que no te da tiempo a realizar…', max_length=150)),
                ('p5', models.CharField(default='Tu amigo te debe dinero…', max_length=150)),
                ('p6', models.CharField(default='Cuando alguien no ha cumplido con algo a lo que se había comprometido…', max_length=150)),
                ('p7', models.CharField(default='Estas esperando en una fila y alguien se "ha colado"…', max_length=150)),
                ('p8', models.CharField(default='Alguien te pide un favor que no estas dispuesto a hacer…', max_length=150)),
                ('p9', models.CharField(default='Cada vez que tengo que llevar la contraria a alguien…', max_length=150)),
                ('p10', models.CharField(default='Cuando me niego a hacer lo que otros me han pedido…', max_length=150)),
                ('p11', models.CharField(default='A la hora de expresar tu opinion, ¿que palabras empleas mas?', max_length=150)),
                ('p12', models.CharField(default='A la hora de expresar tu opinion, ¿como son tus gestos?', max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p1',
            field=models.CharField(default='Mis emociones aparecen sin que yo comprenda o entienda de donde provienen o por que ocurren', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p10',
            field=models.CharField(default='Cuando me siento mal, consigo facilmente identificar la situacion que hizo sentirme mal', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p11',
            field=models.CharField(default='Consigo obtener con facilidad lo que deseo de las otras personas', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p12',
            field=models.CharField(default='Recupero facilmente la calma o mi equilibrio despues de haber vivido una situacinn dificil', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p13',
            field=models.CharField(default='Puedo facilmente explicar las emociones de las personas que me son proximas', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p14',
            field=models.CharField(default='La mayor parte del tiempo, consigo facilmente entender por que las personas sienten lo que sienten', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p15',
            field=models.CharField(default='Cuando estoy triste, me resulta facil recuperar mi buen humor', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p16',
            field=models.CharField(default='Cuando algo me afecta, se inmediatamente que es lo que siento', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p17',
            field=models.CharField(default='Si algo me disgusta, consigo decirlo o expresarlo con calma', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p18',
            field=models.CharField(default='No entiendo por que las personas proximas a mi reaccionan como lo hacen', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p19',
            field=models.CharField(default='Cuando veo a alguien que esta estresado o ansioso, consigo calmarlo facilmente', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p2',
            field=models.CharField(default='No entiendo siempre por que reacciono de la manera que reacciono', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p20',
            field=models.CharField(default='Despues de una discusion, no consigo saber si estoy triste o enfadado', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p21',
            field=models.CharField(default='Uso mis emociones para mejorar las decisiones que tomo en mi vida', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p22',
            field=models.CharField(default='Intento aprender de las situaciones o emociones dificiles', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p23',
            field=models.CharField(default='Los demas me buscan con frecuencia para hablarme de sus problemas personales', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p24',
            field=models.CharField(default='Mis emociones me dicen que cambios tengo que hacer en mi vida', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p25',
            field=models.CharField(default='Es dificil para mi explicar a los otros lo que siento, aunque quiera hacerlo', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p26',
            field=models.CharField(default='No siempre entiendo por que estoy estresado', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p27',
            field=models.CharField(default='Si alguien viniera a mi llorando, no sabria qué hacer', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p28',
            field=models.CharField(default='Tengo dificultades para escuchar a la gente que se queja', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p29',
            field=models.CharField(default='No tengo la actitud adecuada con las personas, porque no consigo percibir su estado emocional', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p3',
            field=models.CharField(default='Si quisiera, podria facilmente manipular las emociones de los otros para obtener lo que quiero', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p30',
            field=models.CharField(default='Consigo facilmente saber lo que las otras personas sienten', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p31',
            field=models.CharField(default='Evito que las personas me hablen de sus problemas', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p32',
            field=models.CharField(default='Se que hacer para motivar a las personas', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p33',
            field=models.CharField(default='Tengo habilidades para subir la moral a las personas', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p34',
            field=models.CharField(default='Tengo dificultades para relacionar lo que una persona siente y las experiencias que ha vivido', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p35',
            field=models.CharField(default='Habitualmente soy capaz de influir en la manera cómo las otras personas se sienten', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p36',
            field=models.CharField(default='Si quisiera, me seria facil hacer que alguien se sienta mal', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p37',
            field=models.CharField(default='Encuentro dificil manejar mis emociones', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p38',
            field=models.CharField(default='Las personas proximas a mi me dicen que no expreso suficientemente lo que siento', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p39',
            field=models.CharField(default='Cuando estoy enfadado, consigo facilmente calmarme', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p4',
            field=models.CharField(default='Se lo que hay que hacer para que las otras personas me apoyen', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p40',
            field=models.CharField(default='A veces me sorprendo con las reacciones de ciertas personas porque no habia percibido que ellas se encontraban de mal humor', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p41',
            field=models.CharField(default='Mis emociones me indican lo que es importante para mi', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p42',
            field=models.CharField(default='Los demas no aceptan la manera en que expreso mis emociones', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p43',
            field=models.CharField(default='Con frecuencia cuando estoy triste, no se el por que', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p44',
            field=models.CharField(default='Con frecuencia me ocurre que no se en que estado emocional estan las personas que me rodean', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p45',
            field=models.CharField(default='Los demas me dicen que soy un buen confidente', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p46',
            field=models.CharField(default='Me siento mal cuando me cuentan alguna dificultad personal', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p47',
            field=models.CharField(default='Cuando estoy delante de una persona enfadada, puedo calmarla facil', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p48',
            field=models.CharField(default='Tengo consciencia de mis emociones desde el momento en que las siento', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p49',
            field=models.CharField(default='Cuando me siento mal, me es difícil saber que emocion exactamente estoy sintiendo', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p5',
            field=models.CharField(default='No consigo entender las reacciones emocionales de las otras personas', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p50',
            field=models.CharField(default='Cuando estoy ante una situacion estresante, me esfuerzo por pensar de una manera que me ayude a permanecer tranquilo', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p6',
            field=models.CharField(default='Cuando me siento bien, consigo diferenciar con facilidad si el motivo es porque estoy contento,orgulloso de mí mismo o relajado', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p7',
            field=models.CharField(default='Se cuando una persona esta enfadada, triste o alegre, aun cuando ella no diga nada', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p8',
            field=models.CharField(default='Consigo encontrar con facilidad las palabras para describir lo que siento', max_length=150),
        ),
        migrations.AlterField(
            model_name='cuestionario_pec',
            name='p9',
            field=models.CharField(default='Nunca me baso en mis emociones para decidir que hago con mi vida', max_length=150),
        ),
        migrations.CreateModel(
            name='Cuestionario_comunicacion_realizado',
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
