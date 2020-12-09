from django.contrib.auth.models import User
from .models import Profile, Cuestionario, Reto_finalizado, Cuestionario_autoestima, Cuestionario_autoestima_respondido, Cuestionario_PEC, Cuestionario_PEC_Realizado, Cuestionario_no, Cuestionario_no_realizado, Cuestionario_comunicacion_efectiva, Cuestionario_comunicacion_realizado, Historial_emociones, Cuestionarios, Preguntas, Respuestas
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

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
        pregunta = Preguntas.objects.create(cuestionario=cuestionario, **validated_data)
        return pregunta
    class Meta:
        model = Preguntas
        fields = (
            'pregunta',
        )

        extra_kwargs = {'titulo': {'write_only': True, 'required': True}}

class RespuestasSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        respuesta = Respuestas.objects.create(**validated_data)
        return respuesta
    class Meta:
        model = Respuestas
        fields = (
            'pregunta',
            'respuesta'
        )


class RetoSerializer(serializers.ModelSerializer):
    def create(self, validated_data, user):
        reto = Reto_finalizado.objects.create(user=user, **validated_data)
        return reto
    class Meta:
        model = Reto_finalizado
        fields = (
            'name',
            'respuesta',
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

class Cuestionario_ComunicacionSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        cuestionario = Cuestionario_comunicacion_efectiva.objects.create(**validated_data)
        return cuestionario

    class Meta:
        model = Cuestionario_comunicacion_efectiva
        fields = (
            'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12'
        )

class Cuestionario_ComunicacionRSerializer(serializers.ModelSerializer):

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
        instance.r10 = validated_data.get('r10', instance.r10),
        instance.r11 = validated_data.get('r11', instance.r11),
        instance.r12 = validated_data.get('r12', instance.r12)

    class Meta:
        model = Cuestionario_comunicacion_realizado
        fields = (
            'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11', 'r12'
        )


class Cuestionario_NOSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        cuestionario = Cuestionario_no.objects.create(**validated_data)
        return cuestionario

    class Meta:
        model = Cuestionario_no
        fields = (
            'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12'
        )

class Cuestionario_NORSerializer(serializers.ModelSerializer):

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
        instance.r10 = validated_data.get('r10', instance.r10),
        instance.r11 = validated_data.get('r11', instance.r11),
        instance.r12 = validated_data.get('r12', instance.r12)

    class Meta:
        model = Cuestionario_no_realizado
        fields = (
            'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11', 'r12'
        )



class Cuestionario_PECRSerializer(serializers.ModelSerializer):

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
        instance.r10 = validated_data.get('r10', instance.r10),
        instance.r11 = validated_data.get('r11', instance.r11),
        instance.r12 = validated_data.get('r12', instance.r12),
        instance.r13 = validated_data.get('r13', instance.r13),
        instance.r14 = validated_data.get('r14', instance.r14),
        instance.r15 = validated_data.get('r15', instance.r15),
        instance.r16 = validated_data.get('r16', instance.r16),
        instance.r17 = validated_data.get('r17', instance.r17),
        instance.r18 = validated_data.get('r18', instance.r18),
        instance.r19 = validated_data.get('r19', instance.r19),
        instance.r20 = validated_data.get('r20', instance.r20),
        instance.r21 = validated_data.get('r21', instance.r21),
        instance.r22 = validated_data.get('r22', instance.r22),
        instance.r23 = validated_data.get('r23', instance.r23),
        instance.r24 = validated_data.get('r24', instance.r24),
        instance.r25 = validated_data.get('r25', instance.r25),
        instance.r26 = validated_data.get('r26', instance.r26),
        instance.r27 = validated_data.get('r27', instance.r27),
        instance.r28 = validated_data.get('r28', instance.r28),
        instance.r29 = validated_data.get('r29', instance.r29),
        instance.r30 = validated_data.get('r30', instance.r30),
        instance.r31 = validated_data.get('r31', instance.r31),
        instance.r32 = validated_data.get('r32', instance.r32),
        instance.r33 = validated_data.get('r33', instance.r33),
        instance.r34 = validated_data.get('r34', instance.r34),
        instance.r35 = validated_data.get('r35', instance.r35),
        instance.r36 = validated_data.get('r36', instance.r36),
        instance.r37 = validated_data.get('r37', instance.r37),
        instance.r38 = validated_data.get('r38', instance.r38),
        instance.r39 = validated_data.get('r39', instance.r39),
        instance.r40 = validated_data.get('r40', instance.r40),
        instance.r41 = validated_data.get('r41', instance.r41),
        instance.r42 = validated_data.get('r42', instance.r42),
        instance.r43 = validated_data.get('r43', instance.r43),
        instance.r44 = validated_data.get('r44', instance.r44),
        instance.r45 = validated_data.get('r45', instance.r45),
        instance.r46 = validated_data.get('r46', instance.r46),
        instance.r47 = validated_data.get('r47', instance.r47),
        instance.r48 = validated_data.get('r48', instance.r48),
        instance.r49 = validated_data.get('r49', instance.r49),
        instance.r50 = validated_data.get('r50', instance.r50)

    class Meta:
        model = Cuestionario_PEC_Realizado
        fields = (
            'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10',
            'r11', 'r12', 'r13', 'r14', 'r15', 'r16', 'r17', 'r18', 'r19', 'r20',
            'r21', 'r22', 'r23', 'r24', 'r25', 'r26', 'r27', 'r28', 'r29', 'r30',
            'r31', 'r32', 'r33', 'r34', 'r35', 'r36', 'r37', 'r38', 'r39', 'r40',
            'r41', 'r42', 'r43', 'r44', 'r45', 'r46', 'r47', 'r48', 'r49', 'r50'
        )


class Cuestionario_PECSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        cuestionario = Cuestionario_PEC.objects.create(**validated_data)
        return cuestionario

    class Meta:
        model = Cuestionario_PEC
        fields = (
            'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10',
            'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20',
            'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p30',
            'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40',
            'p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47', 'p48', 'p49', 'p50'
        )


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
        Cuestionario_PEC_Realizado.objects.create(user=user)
        Cuestionario_comunicacion_realizado.create(user=user)

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

    class Meta:
        model = Profile
        fields = (
            'racha',
            'puntos'
        )



