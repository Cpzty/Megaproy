from django.contrib.auth.models import User
from .models import Profile, Cuestionario, Reto_finalizado, Cuestionario_autoestima, Cuestionario_autoestima_respondido
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class Cuestionario_AESerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        cuestionario = Cuestionario_autoestima.objects.create(**validated_data)
        return cuestionario

    class Meta:
        model = Cuestionario_autoestima
        fields = (
            'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10'
        )

class Cuestionario_AERSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.r1 = validated_data.get('r1', instance.r1),
        instance.r2 = validated_data.get('r2', instance.r2),
        instance.r3 = validated_data.get('r3', instance.r3),
        instance.r4 = validated_data.get('r4', instance.r4),
        instance.r5 = validated_data.get('r5', instance.r5),
        instance.r6 = validated_data.get('r6', instance.r6),
        instance.r7 = validated_data.get('r7', instance.r7),
        instance.r8 = validated_data.get('r8', instance.r8),
        instance.r9 = validated_data.get('r9', instance.r9),
        instance.r10 = validated_data.get('r10', instance.r10)

    class Meta:
        model = Cuestionario_autoestima_respondido
        fields = (
            'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10'
        )


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user)
        Cuestionario_autoestima_respondido.objects.create(user=user)
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
            'puntos'
        )


class RetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reto_finalizado
        fields = (
            'user',
            'reto',
            'finalizado',

        )
