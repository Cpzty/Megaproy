from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

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

