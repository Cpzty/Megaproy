from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()