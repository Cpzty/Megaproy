from .serializers import UserSerializer, ProfileSerializer, CuestionarioSerializer, RetoSerializer, Cuestionario_AESerializer, Cuestionario_AERSerializer, Cuestionario_PECSerializer, Cuestionario_PECRSerializer, Cuestionario_NOSerializer, Cuestionario_NORSerializer, Cuestionario_ComunicacionSerializer, Cuestionario_ComunicacionRSerializer, Historial_emocionesSerializer, CuestionariosSerializer, PreguntasSerializer, InsigniasSerializer, Insignias_usuarioSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Profile, Cuestionario, Reto_finalizado, Cuestionario_autoestima, Cuestionario_autoestima_respondido, Cuestionario_PEC, Cuestionario_PEC_Realizado, Cuestionario_no, Cuestionario_no_realizado, Cuestionario_comunicacion_efectiva, Cuestionario_comunicacion_realizado, Historial_emociones, Cuestionarios, Preguntas, Respuestas, Insignias, Insignias_usuario
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
#from django.template.loader import render_to_string
from django.urls import reverse

from django_rest_passwordreset.signals import reset_password_token_created
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
    }

    # render email text
    #email_html_message = render_to_string('email/user_reset_password.html', context)
    #email_plaintext_message = render_to_string('email/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        "Cambio de contraseña {title}".format(title="Appsertividad"),
        # message:
        'Utiliza este token: {} para cambiar tu contraseña'.format(reset_password_token.key),
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
    #msg.attach_alternative(email_html_message, "text/html")
    msg.send()

class InsigniasView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        insignia = Insignias.objects.filter(titulo=request.POST.get('titulo', 'default'))
        serializer = InsigniasSerializer(insignia, many=True)
        return  Response(serializer.data)

    def post(self, request):
        serializer = InsigniasSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class PreguntasView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        title = request.POST.get('titulo', 'default')

        cuestionarios = Cuestionarios.objects.filter(titulo=title)
        preguntas =  Preguntas.objects.filter(cuestionario__id=cuestionarios[0].id)
        #serializer = PreguntasSerializer(preguntas, many=True)
        dynamyc_preguntas = {}
        for i in range(preguntas.count()):
            dynamyc_preguntas['r'+str(i+1)] = preguntas[i].pregunta

        data = dynamyc_preguntas
        return  JsonResponse(data)

    def put(self, request):
        title = request.POST.get('titulo', 'default')
        id_pregunta = request.POST.get('id_pregunta', 'default')
        cuestionarios = Cuestionarios.objects.filter(titulo=title)
        preguntas = Preguntas.objects.filter(cuestionario__id=cuestionarios[0].id, id=id_pregunta)
        for objec in preguntas:
            objec.pregunta = request.POST.get('modificar_pregunta', '')
            objec.save()

        data = {'status': 'OK'}

        return JsonResponse(data)


    def post(self, request):
        cuestionarios = Cuestionarios.objects.filter(titulo=request.POST.get('titulo', 'default'))
        serializer = PreguntasSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(cuestionario=cuestionarios, validated_data=serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class CuestionariosView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cuestionarios = Cuestionarios.objects.filter(titulo=request.POST.get('titulo', 'default'))
        serializer = CuestionariosSerializer(cuestionarios, many=True)
        return  Response(serializer.data)

    def post(self, request):
        serializer = CuestionariosSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class HistorialEmocionesView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        emocion = request.POST.get('conteo_emociones', 'default')
        if emocion == 'default':
            users =  Historial_emociones.objects.filter(user=request.user, fecha_registrada=request.fecha_registrada)
            serializer = Historial_emocionesSerializer(users, many=True)
            return  Response(serializer.data)

        elif emocion != 'todas':
            H1= Historial_emociones.objects.filter(user=request.user, emocion_inicial=emocion).count()
            data = {
                'emocion': emocion,
                'count': H1
            }
            return JsonResponse(data)

        else:
            E1 = Historial_emociones.objects.filter(user=request.user, emocion_inicial='alegre').count()
            E2 = Historial_emociones.objects.filter(user=request.user, emocion_inicial='caraX').count()
            E3 = Historial_emociones.objects.filter(user=request.user, emocion_inicial='triste').count()
            E4 = Historial_emociones.objects.filter(user=request.user, emocion_inicial='enojado').count()

            data = {
                'alegre': E1,
                'X': E2,
                'triste': E3,
                'enojado': E4
            }
            return JsonResponse(data)


    def post(self, request):
        serializer = Historial_emocionesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=serializer.data, user=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class RetoRecordView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        retos = Reto_finalizado.objects.filter(user=request.user, fecha_registrada=request.fecha_registrada)
        serializer = RetoSerializer(retos)
        return Response(serializer.data)

    def post(self, request):
        serializer = RetoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=serializer.data, user=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class CuestionarioComunicacionRView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = Cuestionario_comunicacion_realizado.objects.filter(user=request.user)
        serializer = Cuestionario_ComunicacionRSerializer(users, many=True)
        return Response(serializer.data)

    def put(self, request):
        users = Cuestionario_comunicacion_realizado.objects.filter(user=request.user)
        for objec in users:
            objec.r1 = request.POST.get('r1', '')
            if objec.r1 == 'a':
                objec.r1 = 0
            elif objec.r1 == 'b':
                objec.r1 = 1
            elif objec.r1 == 'c':
                objec.r1 = 2

            objec.r2 = request.POST.get('r2', '')
            if objec.r2 == 'a':
                objec.r2 = 1
            elif objec.r2 == 'b':
                objec.r2 = 0
            elif objec.r2 == 'c':
                objec.r2 = 2

            objec.r3 = request.POST.get('r3', '')
            if objec.r3 == 'a':
                objec.r3 = 0
            elif objec.r3 == 'b':
                objec.r3 = 2
            elif objec.r3 == 'c':
                objec.r3 = 1

            objec.r4 = request.POST.get('r4', '')
            if objec.r4 == 'a':
                objec.r4 = 0
            elif objec.r4 == 'b':
                objec.r4 = 1
            elif objec.r4 == 'c':
                objec.r4 = 2

            objec.r5 = request.POST.get('r5', '')
            if objec.r5 == 'a':
                objec.r5 = 0
            elif objec.r5 == 'b':
                objec.r5 = 1
            elif objec.r5 == 'c':
                objec.r5 = 2

            objec.r6 = request.POST.get('r6', '')
            if objec.r6 == 'a':
                objec.r6 = 0
            elif objec.r6 == 'b':
                objec.r6 = 2
            elif objec.r6 == 'c':
                objec.r6 = 1

            objec.r7 = request.POST.get('r7', '')
            if objec.r7 == 'a':
                objec.r7 = 1
            elif objec.r7 == 'b':
                objec.r7 = 2
            elif objec.r7 == 'c':
                objec.r7 = 0

            objec.r8 = request.POST.get('r8', '')
            if objec.r8 == 'a':
                objec.r8 = 0
            elif objec.r8 == 'b':
                objec.r8 = 2
            elif objec.r8 == 'c':
                objec.r8 = 1

            objec.r9 = request.POST.get('r9', '')
            if objec.r9 == 'a':
                objec.r9 = 1
            elif objec.r9 == 'b':
                objec.r9 = 0
            elif objec.r9 == 'c':
                objec.r9 = 2

            objec.r10 = request.POST.get('r10', '')
            if objec.r10 == 'a':
                objec.r10 = 1
            elif objec.r10 == 'b':
                objec.r10 = 2
            elif objec.r10 == 'c':
                objec.r10 = 0

            objec.r11 = request.POST.get('r11', '')
            if objec.r11 == 'a':
                objec.r11 = 0
            elif objec.r11 == 'b':
                objec.r11 = 1
            elif objec.r11 == 'c':
                objec.r11 = 2

            objec.r12 = request.POST.get('r12', '')
            if objec.r12 == 'a':
                objec.r12 = 1
            elif objec.r12 == 'b':
                objec.r12 = 0
            elif objec.r12 == 'c':
                objec.r12 = 2

        objec.save()
        serializer = Cuestionario_ComunicacionRSerializer(users, many=True)
        return Response(serializer.data)


class CuestionarioComunicacionView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = Cuestionario_ComunicacionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
            "error": True,
            "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request):
        cuestionario = Cuestionario_comunicacion_efectiva.objects.all().order_by('-id')[0]
        serializer = Cuestionario_ComunicacionSerializer(cuestionario)
        return Response(serializer.data)


class CuestionarioNORView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = Cuestionario_no_realizado.objects.filter(user=request.user)
        serializer = Cuestionario_NORSerializer(users, many=True)
        return Response(serializer.data)

    def put(self, request):
        users = Cuestionario_no_realizado.objects.filter(user=request.user)
        for objec in users:
            objec.r1 = request.POST.get('r1', '')
            if objec.r1 == 'a':
                objec.r1 = 0
            elif objec.r1 == 'b':
                objec.r1 = 2
            elif objec.r1 == 'c':
                objec.r1 = 1

            objec.r2 = request.POST.get('r2', '')
            if objec.r2 == 'a':
                objec.r2 = 2
            elif objec.r2 == 'b':
                objec.r2 = 0
            elif objec.r2 == 'c':
                objec.r2 = 1

            objec.r3 = request.POST.get('r3', '')
            if objec.r3 == 'a':
                objec.r3 = 0
            elif objec.r3 == 'b':
                objec.r3 = 1
            elif objec.r3 == 'c':
                objec.r3 = 2

            objec.r4 = request.POST.get('r4', '')
            if objec.r4 == 'a':
                objec.r4 = 0
            elif objec.r4 == 'b':
                objec.r4 = 2
            elif objec.r4 == 'c':
                objec.r4 = 1

            objec.r5 = request.POST.get('r5', '')
            if objec.r5 == 'a':
                objec.r5 = 0
            elif objec.r5 == 'b':
                objec.r5 = 2
            elif objec.r5 == 'c':
                objec.r5 = 1

            objec.r6 = request.POST.get('r6', '')
            if objec.r6 == 'a':
                objec.r6 = 0
            elif objec.r6 == 'b':
                objec.r6 = 1
            elif objec.r6 == 'c':
                objec.r6 = 2

            objec.r7 = request.POST.get('r7', '')
            if objec.r7 == 'a':
                objec.r7 = 2
            elif objec.r7 == 'b':
                objec.r7 = 1
            elif objec.r7 == 'c':
                objec.r7 = 0

            objec.r8 = request.POST.get('r8', '')
            if objec.r8 == 'a':
                objec.r8 = 0
            elif objec.r8 == 'b':
                objec.r8 = 1
            elif objec.r8 == 'c':
                objec.r8 = 2

            objec.r9 = request.POST.get('r9', '')
            if objec.r9 == 'a':
                objec.r9 = 1
            elif objec.r9 == 'b':
                objec.r9 = 0
            elif objec.r9 == 'c':
                objec.r9 = 2

            objec.r10 = request.POST.get('r10', '')
            if objec.r10 == 'a':
                objec.r10 = 2
            elif objec.r10 == 'b':
                objec.r10 = 1
            elif objec.r10 == 'c':
                objec.r10 = 0

            objec.r11 = request.POST.get('r11', '')
            if objec.r11 == 'a':
                objec.r11 = 0
            elif objec.r11 == 'b':
                objec.r11 = 2
            elif objec.r11 == 'c':
                objec.r11 = 1

            objec.r12 = request.POST.get('r12', '')
            if objec.r12 == 'a':
                objec.r12 = 2
            elif objec.r12 == 'b':
                objec.r12 = 0
            elif objec.r12 == 'c':
                objec.r12 = 1

        objec.save()
        serializer = Cuestionario_NORSerializer(users, many=True)
        return Response(serializer.data)


class CuestionarioNOView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = Cuestionario_NOSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
            "error": True,
            "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request):
        cuestionario = Cuestionario_no.objects.all().order_by('-id')[0]
        serializer = Cuestionario_NOSerializer(cuestionario)
        return Response(serializer.data)


class CuestionarioPECView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = Cuestionario_PECSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
            "error": True,
            "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request):
        cuestionario = Cuestionario_PEC.objects.all().order_by('-id')[0]
        serializer = Cuestionario_PECSerializer(cuestionario)
        return Response(serializer.data)


class CuestionarioPECRView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = Cuestionario_PEC_Realizado.objects.filter(user=request.user)
        serializer = Cuestionario_PECRSerializer(users, many=True)
        return Response(serializer.data)

    def put(self, request):
        users = Cuestionario_PEC_Realizado.objects.filter(user=request.user)
        for objec in users:
            objec.r1 = request.POST.get('r1', 0)
            objec.r2 = request.POST.get('r2', 0)
            objec.r3 = request.POST.get('r3', 0)
            objec.r4 = request.POST.get('r4', 0)
            objec.r5 = request.POST.get('r5', 0)
            objec.r6 = request.POST.get('r6', 0)
            objec.r7 = request.POST.get('r7', 0)
            objec.r8 = request.POST.get('r8', 0)
            objec.r9 = request.POST.get('r9', 0)
            objec.r10 = request.POST.get('r10', 0)
            objec.r11 = request.POST.get('r11', 0)
            objec.r12 = request.POST.get('r12', 0)
            objec.r13 = request.POST.get('r13', 0)
            objec.r14 = request.POST.get('r14', 0)
            objec.r15 = request.POST.get('r15', 0)
            objec.r16 = request.POST.get('r16', 0)
            objec.r17 = request.POST.get('r17', 0)
            objec.r18 = request.POST.get('r18', 0)
            objec.r19 = request.POST.get('r19', 0)
            objec.r20 = request.POST.get('r20', 0)
            objec.r21 = request.POST.get('r21', 0)
            objec.r22 = request.POST.get('r22', 0)
            objec.r23 = request.POST.get('r23', 0)
            objec.r24 = request.POST.get('r24', 0)
            objec.r25 = request.POST.get('r25', 0)
            objec.r26 = request.POST.get('r26', 0)
            objec.r27 = request.POST.get('r27', 0)
            objec.r28 = request.POST.get('r28', 0)
            objec.r29 = request.POST.get('r29', 0)
            objec.r30 = request.POST.get('r30', 0)
            objec.r31 = request.POST.get('r31', 0)
            objec.r32 = request.POST.get('r32', 0)
            objec.r33 = request.POST.get('r33', 0)
            objec.r34 = request.POST.get('r34', 0)
            objec.r35 = request.POST.get('r35', 0)
            objec.r36 = request.POST.get('r36', 0)
            objec.r37 = request.POST.get('r37', 0)
            objec.r38 = request.POST.get('r38', 0)
            objec.r39 = request.POST.get('r39', 0)
            objec.r40 = request.POST.get('r40', 0)
            objec.r41 = request.POST.get('r41', 0)
            objec.r42 = request.POST.get('r42', 0)
            objec.r43 = request.POST.get('r43', 0)
            objec.r44 = request.POST.get('r44', 0)
            objec.r45 = request.POST.get('r45', 0)
            objec.r46 = request.POST.get('r46', 0)
            objec.r47 = request.POST.get('r47', 0)
            objec.r48 = request.POST.get('r48', 0)
            objec.r49 = request.POST.get('r49', 0)
            objec.r50 = request.POST.get('r50', 0)

        objec.save()
        serializer = Cuestionario_PECRSerializer(users, many=True)
        return Response(serializer.data)

class CuestionarioAEView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = Cuestionario_AESerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
            "error": True,
            "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request):
        cuestionario = Cuestionario_autoestima.objects.all().order_by('-id')[0]
        serializer = Cuestionario_AESerializer(cuestionario)
        return Response(serializer.data)

class CuestionarioAERView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = Cuestionario_autoestima_respondido.objects.filter(user=request.user)
        serializer = Cuestionario_AERSerializer(users, many=True)
        return Response(serializer.data)

    def put(self, request):
        users = Cuestionario_autoestima_respondido.objects.filter(user=request.user)
        for objec in users:
            objec.r1 = request.POST.get('r1', 0)
            objec.r2 = request.POST.get('r2', 0)
            objec.r3 = request.POST.get('r3', 0)
            objec.r4 = request.POST.get('r4', 0)
            objec.r5 = request.POST.get('r5', 0)
            objec.r6 = request.POST.get('r6', 0)
            objec.r7 = request.POST.get('r7', 0)
            objec.r8 = request.POST.get('r8', 0)
            objec.r9 = request.POST.get('r9', 0)
            objec.r10 = request.POST.get('r10', 0)

        objec.save()
        serializer = Cuestionario_AERSerializer(users, many=True)
        return Response(serializer.data)

class UserRecordView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        users = User.objects.filter(username=request.user.username)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            print("request data: ", request.data)
            modder = request.data.dict()
            modder['email'] = modder.get('email')
            print('modder: ',modder)
            
            serializer.create(validated_data=modder)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class CuestionarioRecordView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        cuestionarios = Cuestionario.objects.filter(id=id)
        serializer = CuestionarioSerializer(cuestionarios)
        return Response(serializer.data)

class ProfileRecordView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = Profile.objects.filter(user=request.user)
        serializer = ProfileSerializer(users, many=True)
        return Response(serializer.data)

    def put(self, request):
        users = Profile.objects.filter(user=request.user)
        for objec in users:
            if 'racha' in request.POST:
                if request.POST.get('racha', '') == 'reset':
                    objec.racha = 0

                else:
                    objec.racha += 1
                    #no resetear puntos
            if 'puntos' in request.POST:
                objec.puntos = int(objec.puntos) + int(request.POST.get('puntos', ''))

            objec.save()
        serializer = ProfileSerializer(users, many=True)
        return Response(serializer.data)

class ProfileUpView(UpdateView):
    model = Profile
    template_name_suffix = '_form'
    queryset = Profile.objects.all()

    def get_object(self):
        user_ = self.kwargs.get('User')
        return get_object_or_404(Profile, id=user_)