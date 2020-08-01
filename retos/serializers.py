from django.contrib.auth.models import User
from .models import Profile, Cuestionario, Reto_finalizado
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user)
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'email',


        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]


class CuestionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuestionario
        fields = (
            'name',
            'questions_count',
            'description',

        )


class ProfileSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.racha = validated_data.get('racha', instance.racha)
        instance.alegre = validated_data.get('alegre', instance.alegre)
        instance.caraX = validated_data.get('caraX', instance.caraX)
        instance.triste = validated_data.get('triste', instance.triste)
        instance.enojado = validated_data.get('enojado', instance.enojado)

    class Meta:
        model = Profile
        fields = (
            'racha',
            'alegre',
            'caraX',
            'triste',
            'enojado',
            'emocion_inicial',
            'emocion_final',
        )


class RetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reto_finalizado
        fields = (
            'user',
            'reto',
            'finalizado',

        )
