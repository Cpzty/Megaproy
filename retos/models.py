from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

import datetime


class Cuestionario_PEC_Realizado(models.Model):
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

@receiver(post_save, sender=User)
def save_pecr(sender, instance, **kwargs):
    instance.Cuestionario_PEC_Realizado.save()


#p = models.CharField(max_length=150, default='')
class Cuestionario_PEC(models.Model):
    p1 = models.CharField(max_length=150, default='As my emotions arise I dont understand where they come from')
    p2 = models.CharField(max_length=150, default='I dont always understand why I respond in the way I do')
    p3 = models.CharField(max_length=150, default='If I wanted, I could easily influence other people´s emotions to achieve what i want')
    p4 = models.CharField(max_length=150, default='I know what to do to win people over to my cause')
    p5 = models.CharField(max_length=150, default='I am often at a loss to understand other people´s emotional responses')
    p6 = models.CharField(max_length=150, default='When I feel good, I can easily tell whether it is due to being proud of myself, happy or relaxed')
    p7 = models.CharField(max_length=150, default='I can tell whether a person is angry, sad or happy even if they don´t talk to me')
    p8 = models.CharField(max_length=150, default='I am good at describing my feelings')
    p9 = models.CharField(max_length=150, default='I never base my personal life choices on my emotions')
    p10 = models.CharField(max_length=150, default='When I am feeling low, I easily make a link between my feelings and a situation that affected me')
    p11 = models.CharField(max_length=150, default='I can easily get what I want from others')
    p12 = models.CharField(max_length=150, default='I easily manage to calm myself down after a difficult experience')
    p13 = models.CharField(max_length=150, default='I can easily explain the emotional responses of the people around me')
    p14 = models.CharField(max_length=150, default='Most of the time I understand why people feel the way they do')
    p15 = models.CharField(max_length=150, default='When I am sad, I find it easy to cheer myself up')
    p16 = models.CharField(max_length=150, default='When I am touched by something, I immediately know what I feel')
    p17 = models.CharField(max_length=150, default='If I dislike something, I manage to say so in a calm manner')
    p18 = models.CharField(max_length=150, default='I do not understand why the people around me respond the way they do')
    p19 = models.CharField(max_length=150, default='When I see someone who is stressed or anxious, I can easily calm them down')
    p20 = models.CharField(max_length=150, default='During an argument I do not know whether I am angry or sad')
    p21 = models.CharField(max_length=150, default='I use my feelings to improve my choices in life')
    p22 = models.CharField(max_length=150, default='I try to learn from difficult situations or emotions')
    p23 = models.CharField(max_length=150, default='Other people tend to confide in me about personal issues')
    p24 = models.CharField(max_length=150, default='My emotions inform me about changes I should make in my life')
    p25 = models.CharField(max_length=150, default='I find it difficult to explain my feelings to others even if I want to')
    p26 = models.CharField(max_length=150, default='I dont always understand why I am stressed')
    p27 = models.CharField(max_length=150, default='If someone came to me in tears, I would not know what to do')
    p28 = models.CharField(max_length=150, default='I find it difficult to listen to people who are complaining')
    p29 = models.CharField(max_length=150, default='I often take the wrong attitude to people because I was not aware of their emotional state')
    p30 = models.CharField(max_length=150, default='I am good at sensing what others are feeling')
    p31 = models.CharField(max_length=150, default='I feel uncomfortable if people tell me about their problems, so I try to avoid it')
    p32 = models.CharField(max_length=150, default='I know what to do to motivate people')
    p33 = models.CharField(max_length=150, default='I am good at lifting other people´s spirits')
    p34 = models.CharField(max_length=150, default='I find it difficult to establish a link between a person´s response and their personal circumstances')
    p35 = models.CharField(max_length=150, default='I am usually able to influence the way other people feel')
    p36 = models.CharField(max_length=150, default='If I wanted, I could easily make someone feel uneasy')
    p37 = models.CharField(max_length=150, default='I find it difficult to handle my emotions')
    p38 = models.CharField(max_length=150, default='The people around me tell me I dont express my feelings openly')
    p39 = models.CharField(max_length=150, default='When I am angry, I find it easy to calm myself down')
    p40 = models.CharField(max_length=150, default='I am often surprised by people´s responses because I was not aware they were in a bad mood')
    p41 = models.CharField(max_length=150, default='My feelings help me to focus on what is important to me')
    p42 = models.CharField(max_length=150, default='Others dont accept the way I express my emotions')
    p43 = models.CharField(max_length=150, default='When I am sad, I often dont know why')
    p44 = models.CharField(max_length=150, default='Quite often I am not aware of people´s emotional state')
    p45 = models.CharField(max_length=150, default='Other people tell me I make a good confidant')
    p46 = models.CharField(max_length=150, default='I feel uneasy when other people tell me about something that is difficult for them')
    p47 = models.CharField(max_length=150, default='When I am confronted with an angry person, I can easily calm them down')
    p48 = models.CharField(max_length=150, default='I am aware of my emotions as soon as they arise')
    p49 = models.CharField(max_length=150, default='When I am feeling low, I find it difficult to know exactly what kind of emotion it is I am feeling')
    p50 = models.CharField(max_length=150, default='In a stressful situation I usually think in a way that helps me stay calm')

#historial de emociones
#falta serializador y view
class Historial_emociones(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    emocion_inicial = models.CharField(max_length=50, default='')
    emocion_final = models.CharField(max_length=50, default='')
    fecha_registrada = models.DateTimeField(default=datetime.date.today)

#cuestionario autoestima rosenberg
class Cuestionario_autoestima(models.Model):
    p1 = models.CharField(max_length=150, default='I feel that I am a person of worth, at least on an equal plane with others')
    p2 = models.CharField(max_length=150, default='I feel that I have a number of good qualities')
    p3 = models.CharField(max_length=150, default='All in all, I am inclined to feel that I am a failure (R)')
    p4 = models.CharField(max_length=150, default='I am able to do things as well as most people')
    p5 = models.CharField(max_length=150, default='I feel I do not have much to be proud of (R)')
    p6 = models.CharField(max_length=150, default='I take a positive attitude toward myself')
    p7 = models.CharField(max_length=150, default='On the whole, I am satisfied with myself')
    p8 = models.CharField(max_length=150, default='I wish I could have more respect for myself (R)')
    p9 = models.CharField(max_length=150, default='I certainly feel useless at times (R)')
    p10 = models.CharField(max_length=150, default='At times I think that I am no good at all (R)')




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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    racha = models.IntegerField(default=0)
    #caritas
    alegre = models.IntegerField(default=0)
    caraX = models.IntegerField(default=0)
    triste = models.IntegerField(default=0)
    enojado = models.IntegerField(default=0)
    #emocion inicial capturada
    emocion_inicial = models.CharField(max_length=50, default='')
    emocion_final = models.CharField(max_length=50, default='')
    #puntaje
    puntos = models.IntegerField(default=0)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reto = models.ForeignKey(Reto, on_delete=models.CASCADE)
    finalizado = models.BooleanField(default=False)


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

