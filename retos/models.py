from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

import datetime

class Cuestionarios(models.Model):
    titulo = models.CharField(max_length=75, blank=False)

class Preguntas(models.Model):
    cuestionario = models.ManyToManyField(Cuestionarios, blank=False)
    pregunta = models.CharField(max_length=150, blank=False)


class Respuestas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    pregunta = models.ForeignKey(Preguntas, on_delete=models.CASCADE, default=None)
    respuesta = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])


class Cuestionario_comunicacion_realizado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    r1 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r2 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r3 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r4 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r5 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r6 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r7 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r8 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r9 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r10 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r11 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r12 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])

@receiver(post_save, sender=User)
def create_comur(sender, instance, created, **kwargs):
    if created:
        Cuestionario_comunicacion_realizado.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_nor(sender, instance, **kwargs):
#    instance.Cuestionario_no_realizado.save()


class Cuestionario_comunicacion_efectiva(models.Model):
    p1 = models.CharField(max_length=150, default='Cuando se que tengo derecho a algo (por ejemplo quejarme, expresar mi opinion, etcetera')
    p2 = models.CharField(max_length=150, default='En las situaciones en las que no estoy de acuerdo con la opinion del otro…')
    p3 = models.CharField(max_length=150, default='Tus intereses chocan con los de tu pareja, amigo… ¿que haces?…')
    p4 = models.CharField(max_length=150, default='En el trabajo te piden hacer una tarea que no te da tiempo a realizar…')
    p5 = models.CharField(max_length=150, default='Tu amigo te debe dinero…')
    p6 = models.CharField(max_length=150, default='Cuando alguien no ha cumplido con algo a lo que se había comprometido…')
    p7 = models.CharField(max_length=150, default='Estas esperando en una fila y alguien se "ha colado"…')
    p8 = models.CharField(max_length=150, default='Alguien te pide un favor que no estas dispuesto a hacer…')
    p9 = models.CharField(max_length=150, default='Cada vez que tengo que llevar la contraria a alguien…')
    p10 = models.CharField(max_length=150, default='Cuando me niego a hacer lo que otros me han pedido…')
    p11 = models.CharField(max_length=150, default='A la hora de expresar tu opinion, ¿que palabras empleas mas?')
    p12 = models.CharField(max_length=150, default='A la hora de expresar tu opinion, ¿como son tus gestos?')


class Cuestionario_no_realizado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    r1 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r2 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r3 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r4 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r5 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r6 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r7 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r8 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r9 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r10 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r11 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    r12 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])

@receiver(post_save, sender=User)
def create_nor(sender, instance, created, **kwargs):
    if created:
        Cuestionario_no_realizado.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_nor(sender, instance, **kwargs):
#    instance.Cuestionario_no_realizado.save()


#p = models.CharField(max_length=150, default='')
class Cuestionario_no(models.Model):
    p1 = models.CharField(max_length=150, default='Mi compañero de trabajo me pide que haga un trabajo que no me corresponde…')
    p2 = models.CharField(max_length=150, default='Cuando por la calle me paran para venderme algo, poner una firma, darme propaganda…')
    p3 = models.CharField(max_length=150, default='Cuando alguien está contando una historia y yo sé que no ha ocurrido de esa manera…')
    p4 = models.CharField(max_length=150, default='Mi jefe me pide que haga un trabajo que no teníamos previsto y para ello tengo que sacrificar tiempo personal…')
    p5 = models.CharField(max_length=150, default='Cuando me ofrecen otra copa y yo ya no quiero más…')
    p6 = models.CharField(max_length=150, default='Cuando me proponen ir al cine a ver una película que yo no quiero')
    p7 = models.CharField(max_length=150, default='Cuando me quieren vender algo que no me convence después de que me han estado atendiendo un largo rato…')
    p8 = models.CharField(max_length=150, default='Cuando mi pareja me propone hacer un plan que no me apetece en absoluto…')
    p9 = models.CharField(max_length=150, default='Si alguien que tampoco me gusta tanto me invita a salir…')
    p10 = models.CharField(max_length=150, default='En la sala de espera del médico o esperando una fila para pagar, alguien me pide pasar antes que yo…')
    p11 = models.CharField(max_length=150, default='Cuando un “listo/a” me quita el sitio de aparcamiento por el que yo estaba esperando…')
    p12 = models.CharField(max_length=150, default='Cuando mi familia me dice que vaya a comer con ellos un día que me viene realmente mal…')

class Cuestionario_PEC_Realizado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    r1 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r2 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r3 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r4 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r5 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r6 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r7 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r8 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r9 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r10 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r11 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r12 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r13 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r14 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r15 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r16 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r17 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r18 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r19 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r20 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r21 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r22 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r23 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r24 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r25 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r26 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r27 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r28 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r29 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r30 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r31 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r32 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r33 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r34 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r35 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r36 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r37 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r38 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r39 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r40 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r41 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r42 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r43 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r44 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r45 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r46 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r47 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r48 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r49 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    r50 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])

@receiver(post_save, sender=User)
def create_pecr(sender, instance, created, **kwargs):
    if created:
        Cuestionario_PEC_Realizado.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_pecr(sender, instance, **kwargs):
#    instance.Cuestionario_PEC_Realizado.save()



#p = models.CharField(max_length=150, default='')
class Cuestionario_PEC(models.Model):
    p1 = models.CharField(max_length=150, default='Mis emociones aparecen sin que yo comprenda o entienda de donde provienen o por que ocurren')
    p2 = models.CharField(max_length=150, default='No entiendo siempre por que reacciono de la manera que reacciono')
    p3 = models.CharField(max_length=150, default='Si quisiera, podria facilmente manipular las emociones de los otros para obtener lo que quiero')
    p4 = models.CharField(max_length=150, default='Se lo que hay que hacer para que las otras personas me apoyen')
    p5 = models.CharField(max_length=150, default='No consigo entender las reacciones emocionales de las otras personas')
    p6 = models.CharField(max_length=150, default='Cuando me siento bien, consigo diferenciar con facilidad si el motivo es porque estoy contento,orgulloso de mí mismo o relajado')
    p7 = models.CharField(max_length=150, default='Se cuando una persona esta enfadada, triste o alegre, aun cuando ella no diga nada')
    p8 = models.CharField(max_length=150, default='Consigo encontrar con facilidad las palabras para describir lo que siento')
    p9 = models.CharField(max_length=150, default='Nunca me baso en mis emociones para decidir que hago con mi vida')
    p10 = models.CharField(max_length=150, default='Cuando me siento mal, consigo facilmente identificar la situacion que hizo sentirme mal')
    p11 = models.CharField(max_length=150, default='Consigo obtener con facilidad lo que deseo de las otras personas')
    p12 = models.CharField(max_length=150, default='Recupero facilmente la calma o mi equilibrio despues de haber vivido una situacinn dificil')
    p13 = models.CharField(max_length=150, default='Puedo facilmente explicar las emociones de las personas que me son proximas')
    p14 = models.CharField(max_length=150, default='La mayor parte del tiempo, consigo facilmente entender por que las personas sienten lo que sienten')
    p15 = models.CharField(max_length=150, default='Cuando estoy triste, me resulta facil recuperar mi buen humor')
    p16 = models.CharField(max_length=150, default='Cuando algo me afecta, se inmediatamente que es lo que siento')
    p17 = models.CharField(max_length=150, default='Si algo me disgusta, consigo decirlo o expresarlo con calma')
    p18 = models.CharField(max_length=150, default='No entiendo por que las personas proximas a mi reaccionan como lo hacen')
    p19 = models.CharField(max_length=150, default='Cuando veo a alguien que esta estresado o ansioso, consigo calmarlo facilmente')
    p20 = models.CharField(max_length=150, default='Despues de una discusion, no consigo saber si estoy triste o enfadado')
    p21 = models.CharField(max_length=150, default='Uso mis emociones para mejorar las decisiones que tomo en mi vida')
    p22 = models.CharField(max_length=150, default='Intento aprender de las situaciones o emociones dificiles')
    p23 = models.CharField(max_length=150, default='Los demas me buscan con frecuencia para hablarme de sus problemas personales')
    p24 = models.CharField(max_length=150, default='Mis emociones me dicen que cambios tengo que hacer en mi vida')
    p25 = models.CharField(max_length=150, default='Es dificil para mi explicar a los otros lo que siento, aunque quiera hacerlo')
    p26 = models.CharField(max_length=150, default='No siempre entiendo por que estoy estresado')
    p27 = models.CharField(max_length=150, default='Si alguien viniera a mi llorando, no sabria qué hacer')
    p28 = models.CharField(max_length=150, default='Tengo dificultades para escuchar a la gente que se queja')
    p29 = models.CharField(max_length=150, default='No tengo la actitud adecuada con las personas, porque no consigo percibir su estado emocional')
    p30 = models.CharField(max_length=150, default='Consigo facilmente saber lo que las otras personas sienten')
    p31 = models.CharField(max_length=150, default='Evito que las personas me hablen de sus problemas')
    p32 = models.CharField(max_length=150, default='Se que hacer para motivar a las personas')
    p33 = models.CharField(max_length=150, default='Tengo habilidades para subir la moral a las personas')
    p34 = models.CharField(max_length=150, default='Tengo dificultades para relacionar lo que una persona siente y las experiencias que ha vivido')
    p35 = models.CharField(max_length=150, default='Habitualmente soy capaz de influir en la manera cómo las otras personas se sienten')
    p36 = models.CharField(max_length=150, default='Si quisiera, me seria facil hacer que alguien se sienta mal')
    p37 = models.CharField(max_length=150, default='Encuentro dificil manejar mis emociones')
    p38 = models.CharField(max_length=150, default='Las personas proximas a mi me dicen que no expreso suficientemente lo que siento')
    p39 = models.CharField(max_length=150, default='Cuando estoy enfadado, consigo facilmente calmarme')
    p40 = models.CharField(max_length=150, default='A veces me sorprendo con las reacciones de ciertas personas porque no habia percibido que ellas se encontraban de mal humor')
    p41 = models.CharField(max_length=150, default='Mis emociones me indican lo que es importante para mi')
    p42 = models.CharField(max_length=150, default='Los demas no aceptan la manera en que expreso mis emociones')
    p43 = models.CharField(max_length=150, default='Con frecuencia cuando estoy triste, no se el por que')
    p44 = models.CharField(max_length=150, default='Con frecuencia me ocurre que no se en que estado emocional estan las personas que me rodean')
    p45 = models.CharField(max_length=150, default='Los demas me dicen que soy un buen confidente')
    p46 = models.CharField(max_length=150, default='Me siento mal cuando me cuentan alguna dificultad personal')
    p47 = models.CharField(max_length=150, default='Cuando estoy delante de una persona enfadada, puedo calmarla facil')
    p48 = models.CharField(max_length=150, default='Tengo consciencia de mis emociones desde el momento en que las siento')
    p49 = models.CharField(max_length=150, default='Cuando me siento mal, me es difícil saber que emocion exactamente estoy sintiendo')
    p50 = models.CharField(max_length=150, default='Cuando estoy ante una situacion estresante, me esfuerzo por pensar de una manera que me ayude a permanecer tranquilo')

#historial de emociones
#falta serializador y view
class Historial_emociones(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    emocion_inicial = models.CharField(max_length=50, default='')
    emocion_final = models.CharField(max_length=50, default='')
    fecha_registrada = models.DateTimeField(default=datetime.date.today)

#cuestionario autoestima rosenberg
#class Cuestionario_autoestima(models.Model):
    #p1 = models.CharField(max_length=150, default='I feel that I am a person of worth, at least on an equal plane with others')
    #p2 = models.CharField(max_length=150, default='I feel that I have a number of good qualities')
    #p3 = models.CharField(max_length=150, default='All in all, I am inclined to feel that I am a failure (R)')
    #p4 = models.CharField(max_length=150, default='I am able to do things as well as most people')
    #p5 = models.CharField(max_length=150, default='I feel I do not have much to be proud of (R)')
    #p6 = models.CharField(max_length=150, default='I take a positive attitude toward myself')
   # p7 = models.CharField(max_length=150, default='On the whole, I am satisfied with myself')
  #  p8 = models.CharField(max_length=150, default='I wish I could have more respect for myself (R)')
 #   p9 = models.CharField(max_length=150, default='I certainly feel useless at times (R)')
#    p10 = models.CharField(max_length=150, default='At times I think that I am no good at all (R)')


class Cuestionario_autoestima(models.Model):
    p1 = models.CharField(max_length=150, default='Siento que soy una persona digna de aprecio, al menos en igual  medida que los demás')
    p2 = models.CharField(max_length=150, default='Me inclino a pensar que, en conjunto, soy un fracasado')
    p3 = models.CharField(max_length=150, default='Creo que tengo varias cualidades buenas')
    p4 = models.CharField(max_length=150, default='Puedo hacer las cosas tan bien como la mayoría de la gente')
    p5 = models.CharField(max_length=150, default='Creo que no tengo muchos motivos para sentirme orgulloso de mí')
    p6 = models.CharField(max_length=150, default='Tengo una actitud positiva hacia mí mismo')
    p7 = models.CharField(max_length=150, default='En general, estoy satisfecho conmigo mismo')
    p8 = models.CharField(max_length=150, default='Desearía valorarme más a mí mismo')
    p9 = models.CharField(max_length=150, default='A veces me siento verdaderamente inútil')
    p10 = models.CharField(max_length=150, default='A veces pienso que no sirvo para nada')



class Cuestionario_autoestima_respondido(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    r1 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    r2 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    r3 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    r4 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    r5 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    r6 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    r7 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    r8 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    r9 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    r10 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])

@receiver(post_save, sender=User)
def create_aer(sender, instance, created, **kwargs):
    if created:
        Cuestionario_autoestima_respondido.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_aer(sender, instance, **kwargs):
    instance.cuestionario_autoestima_respondido.save()

#
#class Estadísticas_emociones(models.Model):
    #User = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    #emoción_registrada = models.CharField(max_length=50, default='')
    #fecha_registrada = models.DateTimeField(default=datetime.date.today)
#

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    racha = models.IntegerField(default=0)
    #puntaje
    puntos = models.IntegerField(default=0)
    cantidad_retos_realizados = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Reto(models.Model):
    description = models.CharField(max_length=1000)

class Caso_4p(models.Model):
    pregunta1 = models.CharField(max_length=250)
    pregunta2 = models.CharField(max_length=250)
    pregunta3 = models.CharField(max_length=250)
    pregunta4 = models.CharField(max_length=250)

class Caso_4p_finalizado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    pregunta1 = models.CharField(max_length=250)
    pregunta2 = models.CharField(max_length=250)
    pregunta3 = models.CharField(max_length=250)
    pregunta4 = models.CharField(max_length=250)


class Reto_finalizado(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name  = models.CharField(max_length=75, default='')
    respuesta = models.CharField(max_length=250, default='')
    fecha_registrada = models.DateTimeField(default=datetime.date.today)


class Cuestionario(models.Model):
    name = models.CharField(max_length=1000)
    questions_count = models.IntegerField(default=0)
    description = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    slug = models.SlugField()
    roll_out = models.BooleanField(default=False)
class Meta:
    ordering = ['created']
    verbose_name_plural ="Cuestionarios"
    def __str__(self):
        return self.name

class Pregunta(models.Model):
    cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)
    label = models.CharField(max_length=1000)
    order = models.IntegerField(default=0)
    def __str__(self):
        return self.label

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return self.text

class CuestionarioRespondido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)
    correct_answers = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
class Respuesta_final(models.Model):
    respondido = models.ForeignKey(CuestionarioRespondido, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(Respuesta,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.question.label

    @receiver(post_save, sender=Cuestionario)
    def set_default_quiz(sender, instance, created,**kwargs):
        cuestionario = Cuestionario.objects.filter(id = instance.id)
        cuestionario.update(questions_count=instance.pregunta_set.filter(cuestionario=instance.pk).count())
    @receiver(post_save, sender=Pregunta)
    def set_default(sender, instance, created,**kwargs):
        cuestionario = Cuestionario.objects.filter(id = instance.cuestionario.id)
        cuestionario.update(questions_count=instance.cuestionario.question_set.filter(cuestionario=instance.cuestionario.pk).count())
    @receiver(pre_save, sender=Cuestionario)
    def slugify_title(sender, instance, *args, **kwargs):
        instance.slug = slugify(instance.name)

