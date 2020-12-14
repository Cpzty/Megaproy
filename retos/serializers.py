from django.contrib.auth.models import User
from .models import Profile, Reto_finalizado, Historial_emociones, Cuestionarios, Preguntas, Respuestas, Insignias, Insignias_usuario, Comentarios, Frases
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

class FrasesSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        frase = Frases.objects.create(**validated_data)
        return frase

    class Meta:
        model = Frases
        fields = (
            'reto',
            'frase'
        )

class ComentarioSerializer(serializers.ModelSerializer):
    def create(self, validated_data, user):
        comentario = Comentarios.objects.create(user=user, **validated_data)
        return comentario

    class Meta:
        model = Comentarios
        fields = (
            'titulo',
            'descripcion',
        )

        extra_kwargs = {'all_comments': {'write_only': True, 'required': False}}


class Insignias_usuarioSerializer(serializers.ModelSerializer):
    def create(self, validated_data, user, insignia_obtenida):
        insignia_usuario = Insignias_usuario.objects.create(user=user, **validated_data)
        insignia_usuario.insignia_obtenida.set(insignia_obtenida)
        return insignia_usuario
    class Meta:
        model = Insignias_usuario
        fields = (
            'fecha_registrada',
        )

        extra_kwargs = {
            'titulo_insignia': {'write_only': True, 'required': False},
            'titulo_cuestionario': {'write_only': True, 'required': False},
            'id_insignia': {'write_only': True, 'required': False},
        }


class InsigniasSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        insignia = Insignias.objects.create(**validated_data)
        return insignia
    class Meta:
        model = Insignias
        fields = (
            'titulo',
            'descripcion',
        )


class CuestionariosSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        cuestionario = Cuestionarios.objects.create(**validated_data)
        return cuestionario
    class Meta:
        model = Cuestionarios
        fields = (
            'titulo',
        )

class PreguntasSerializer(serializers.ModelSerializer):
    def create(self, validated_data, cuestionario):
        pregunta = Preguntas.objects.create(**validated_data)
        pregunta.cuestionario.set(cuestionario)
        return pregunta
    class Meta:
        model = Preguntas
        fields = (
            'pregunta',
        )

        extra_kwargs = {
            'titulo': {'write_only': True, 'required': True},
            'id_pregunta': {'write_only': True, 'required': False},
            'modificar_pregunta': {'write_only': True, 'required': False}
        }

class RespuestasSerializer(serializers.ModelSerializer):
    def create(self, validated_data, user, pregunta):
        respuesta = Respuestas.objects.create(user=user, **validated_data)
        respuesta.pregunta.set(pregunta)
        return respuesta
    class Meta:
        model = Respuestas
        fields = (
            'respuesta',
        )

        extra_kwargs = {
            'pregunta': {'required': True},
            'id_respuesta': {'write_only': True, 'required': False},
            'modificar_respuesta': {'write_only': True, 'required': False},
            'titulo_cuestionario': {'write_only': True, 'required': False},

        }


class RetoSerializer(serializers.ModelSerializer):
    def create(self, validated_data, user):
        reto = Reto_finalizado.objects.create(user=user, **validated_data)
        return reto
    class Meta:
        model = Reto_finalizado
        fields = (
            'name',
            'respuesta',
            'puntos',
            'fecha_registrada',
        )

class Historial_emocionesSerializer(serializers.ModelSerializer):
    def create(self, validated_data, user):
        historial = Historial_emociones.objects.create(user=user, **validated_data)
        return historial

    class Meta:
        model = Historial_emociones
        fields = (
            'emocion_inicial',
            'emocion_final',
            'fecha_registrada'
        )

        extra_kwargs = {'conteo_emociones': {'write_only': True, 'required': False}}


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user)
        #Cuestionario_autoestima_respondido.objects.create(user=user)
        #Cuestionario_PEC_Realizado.objects.create(user=user)
        #Cuestionario_comunicacion_realizado.create(user=user)

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

        extra_kwargs = {'ranking': {'write_only': True, 'required': False}}


class ProfileSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.racha = validated_data.get('racha', instance.racha)

    class Meta:
        model = Profile
        fields = (
            'racha',
            'autoestima_finalizado',
            'pec_finalizado',
            'comodecirqueno_finalizado',
            'comunicacion_finalizado',
        )



