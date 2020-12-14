from .serializers import UserSerializer, ProfileSerializer, RetoSerializer, Historial_emocionesSerializer, CuestionariosSerializer, PreguntasSerializer, InsigniasSerializer, Insignias_usuarioSerializer, RespuestasSerializer, ComentarioSerializer, FrasesSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Profile, Reto_finalizado, Historial_emociones, Cuestionarios, Preguntas, Respuestas, Insignias, Insignias_usuario, Comentarios, Frases
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
#from django.template.loader import render_to_string
from django.urls import reverse

from django_rest_passwordreset.signals import reset_password_token_created
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

import random

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

class FrasesView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = FrasesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create( validated_data=serializer.data)

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
        data = {}
        reto = request.POST.get('reto', 'default')
        if reto != 'default':
            frases_count = Frases.objects.filter(reto=reto).count()
            frase_seleccionada = random.randint(0, frases_count-1)
            data['frase'] = Frases.objects.filter(reto=reto)[frase_seleccionada].frase
        else:
            data['reto'] = 'no se especifico reto'

        return JsonResponse(data)

class ComentariosView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ComentarioSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(user=request.user ,validated_data=serializer.data)

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
        data = {}
        all_comments = request.POST.get('all_comments', 'default')
        if all_comments == 'default':
            comentarios = Comentarios.objects.filter(user=request.user)
            for i in range(comentarios.count()):
                data['titulo' + str(i)] = comentarios[i].titulo
                data['comentario' + str(i)] = comentarios[i].descripcion

        else:
            comentarios = Comentarios.objects.all()
            for i in range(comentarios.count()):
                username = User.objects.get(id=comentarios[i].user_id).username
                data['user' + str(i)] = username
                data['titulo' + str(i)] = comentarios[i].titulo
                data['comentario' + str(i)] = comentarios[i].descripcion

        return JsonResponse(data)

class Insignias_usuarioView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        identifier = request.POST.get('titulo_insignia', 'default')
        insignia = Insignias.objects.filter(titulo=identifier)
        serializer = Insignias_usuarioSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(user=request.user, insignia_obtenida=insignia, validated_data=serializer.data)

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
        #id_insignia = request.POST.get('id_insignia', 'default')
        insignias = Insignias_usuario.objects.all().filter(user=request.user)
        insignias_count = insignias.count()
        data = {}
        contador = 0
        for i in range(insignias_count):
            insignias2 = Insignias_usuario.objects.get(id= insignias[i].id).insignia_obtenida.all()
            data['t' + str(contador+1)] = insignias2[0].titulo
            data['d' + str(contador+1)] = insignias2[0].descripcion
            data['fecha' + str(contador+1)] = insignias[i].fecha_registrada
            contador += 1

        return JsonResponse(data)

    def delete(self, request):
        id_insignia = request.POST.get('id_insignia', 'default')
        insignia = Insignias_usuario.objects.filter(id=id_insignia)
        for objec in insignia:
            objec.delete()
        data = {'remover': 'ok'}
        return JsonResponse(data)


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

class RespuestasView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        #paso 1 obtener todas las preguntas de usuario
        #paso 2 obtener preguntas de un cuestionario
        title = request.POST.get('titulo_cuestionario', 'default')
        cuestionarios = Cuestionarios.objects.filter(titulo=title)
        preguntas = Preguntas.objects.all()
        ids_preguntas = []
        for i in range(preguntas.count()):
            ids_preguntas.append(preguntas[i].id)

        ids_preguntas2 = []
        for i in range(len(ids_preguntas)):
            preguntas2 = Preguntas.objects.get(id=ids_preguntas[i]).cuestionario.all()
            if preguntas2[0].id == cuestionarios[0].id:
                ids_preguntas2.append(preguntas[i].id)

        #paso 3 obtener todas las respuestas de un usuario
        respuestas = Respuestas.objects.filter(user=request.user)
        ids_respuestas = []
        for i in range(respuestas.count()):
            ids_respuestas.append(respuestas[i].id)

        dynamyc_respuestas = {}
        contador = 1
        for i in range(len(ids_respuestas)):
            respuestas2 = Respuestas.objects.get(id=ids_respuestas[i]).pregunta.all()
            if respuestas2[0].id in ids_preguntas2:
                dynamyc_respuestas['r' + str(contador)] = respuestas[i].respuesta
                contador+= 1


        data = dynamyc_respuestas
        return JsonResponse(data)

    def put(self, request):
        id_respuesta = request.POST.get('id_respuesta', 'default')
        respuestas = Respuestas.objects.filter(id=id_respuesta)
        for objec in respuestas:
            objec.respuesta = request.POST.get('modificar_respuesta', '')
            objec.save()
        data = {'status': 'OK'}

        return JsonResponse(data)


    def delete(self, request):
        id_respuesta = request.POST.get('id_respuesta', 'default')
        respuestas = Respuestas.objects.filter(id=id_respuesta)
        for objec in respuestas:
            objec.delete()
        data = {'remover': 'ok'}
        return JsonResponse(data)

    def post(self, request):
        identifier = request.POST.get('pregunta', 'default')
        preguntas = Preguntas.objects.filter(pregunta=identifier)
        #data = serializers.serialize('json', respuesta.values())
        serializer = RespuestasSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(user=request.user, pregunta=preguntas, validated_data=serializer.data)

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
            dynamyc_preguntas['p'+str(i+1)] = preguntas[i].pregunta

        data = dynamyc_preguntas
        return  JsonResponse(data)

    def delete(self, request):
        title = request.POST.get('titulo', 'default')
        id_pregunta = request.POST.get('id_pregunta', 'default')
        cuestionarios = Cuestionarios.objects.filter(titulo=title)
        preguntas = Preguntas.objects.filter(cuestionario__id=cuestionarios[0].id, id=id_pregunta)
        for objec in preguntas:
            objec.delete()
        data = {'remover': 'ok'}
        return JsonResponse(data)

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
        retos = Reto_finalizado.objects.filter(user=request.user)
        data = {}
        contador = 0
        for objec in retos:
            data['reto'+ str(contador+1)] = objec.name
            data['respuesta' + str(contador + 1)] = objec.respuesta
            contador += 1
        data['cantidad total'] = retos.count()

        return JsonResponse(data)

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



class ProfileRecordView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.filter(user=request.user)
        data = {}
        ranks = request.POST.get('ranking', 'default')
        if ranks == 'default':
            data['racha'] = profile[0].racha
            data['puntos'] =  Reto_finalizado.objects.filter(user=request.user).count() * 10

        elif ranks == 'puntos':
            ids_usuarios = []
            retos = Reto_finalizado.objects.all()
            for user in retos:
                if user.user_id not in ids_usuarios:
                    ids_usuarios.append(user.user_id)
            #print('ids: ', ids_usuarios)
            data2 = {}
            count_usuario = []
            conteo_puntos = 0
            for i in range(len(ids_usuarios)):
                reto = Reto_finalizado.objects.filter(user_id=ids_usuarios[i]).count()
                username = User.objects.get(id=ids_usuarios[i]).username
                puntos = Reto_finalizado.objects.filter(user_id=ids_usuarios[i])
                data2['retos' + str(i)] = [reto, username]
                for j in range(puntos.count()):
                    conteo_puntos += puntos[j].puntos
                count_usuario.append(conteo_puntos)
                conteo_puntos = 0
            count_usuario.sort(reverse=True)
            sort_data2 = sorted(data2.items(), key=lambda x: x[1][0], reverse=True)
            for i in range(len(ids_usuarios)):
                #print(sort_data2)
                data['username' + str(i)] = sort_data2[i][1][1]
                #sort_data2[i][1][2] son puntos
                #print('sorted: ', sort_data2)
                data['retos' + str(i)] = sort_data2[i][1][0]

                data['puntos' + str(i)] = count_usuario[i]

                #rework para obtener puntos a traves de retos realizados

            pass
         #   profiles = Profile.objects.all().order_by('-puntos')
          #  profile_ids = []
           # for user in profiles:
            #    profile_ids.append(user.user_id)
            #usernames = []
            #for i in range(profiles.count()):
             #   usernames.append(User.objects.get(id=profile_ids[i]).username)

            #data
            #for i in range(profiles.count()):
             #   data['user' + str(i)] = usernames[i]
              #  data['puntos' + str(i)] = profiles[i].puntos
                #data['id' + str(i)] = profile_ids[i]

        elif ranks == 'insignias':
            ids_usuarios = []
            usuarios_insignia = Insignias_usuario.objects.all()
            for user in usuarios_insignia:
                if user.user_id not in ids_usuarios:
                    ids_usuarios.append(user.user_id)
            for i in range(len(ids_usuarios)):
                cantidad_insignias = Insignias_usuario.objects.filter(user_id=ids_usuarios[i]).count()
                username = User.objects.get(id=ids_usuarios[i]).username
                data['username' + str(i)] = username
                data['insignias' + str(i)] = cantidad_insignias

        elif ranks == 'comentarios':
            ids_usuarios = []
            comentarios = Comentarios.objects.all()
            for user in comentarios:
                if user.user_id not in ids_usuarios:
                    ids_usuarios.append(user.user_id)

            data2 = {}
            for i in range(len(ids_usuarios)):
                comentario = Comentarios.objects.filter(user_id=ids_usuarios[i]).count()
                username = User.objects.get(id=ids_usuarios[i]).username
                data2['comentarios' + str(i)] = [comentario, username]
            sort_data2 = sorted(data2.items(), key=lambda x: x[1][0], reverse=True)
            for i in range(len(ids_usuarios)):
                data['username' + str(i)] = sort_data2[i][1][1]
                data['comentarios' + str(i)] = sort_data2[i][1][0]


        elif ranks == 'retos':
            ids_usuarios = []
            usuarios_retos = Reto_finalizado.objects.all()
            for user in usuarios_retos:
                if user.user_id not in ids_usuarios:
                    ids_usuarios.append(user.user_id)
            data2 = {}
            for i in range(len(ids_usuarios)):
                cantidad_retos = Reto_finalizado.objects.filter(user_id=ids_usuarios[i]).count()
                username = User.objects.get(id=ids_usuarios[i]).username
                data2['username' + str(i)] = [cantidad_retos, username]
            sort_data2 = sorted(data2.items(), key=lambda x: x[1][0], reverse=True)
            for i in range(len(ids_usuarios)):
                data['username' + str(i)] = sort_data2[i][1][1]
                data['retos' + str(i)] = sort_data2[i][1][0]
                #data['retos' + str(i)] = cantidad_retos

        elif ranks == 'racha':
            profiles = Profile.objects.all().order_by('-racha')
            profile_ids = []
            for user in profiles:
                profile_ids.append(user.user_id)
            usernames = []
            for i in range(profiles.count()):
                usernames.append(User.objects.get(id=profile_ids[i]).username)

            # data
            for i in range(profiles.count()):
                data['user' + str(i)] = usernames[i]
                data['racha' + str(i)] = profiles[i].racha
                # data['id' + str(i)] = profile_ids[i]

        return JsonResponse(data)

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

            if 'autoestima_finalizado' in request.POST:
                objec.autoestima_finalizado = True

            if 'pec_finalizado' in request.POST:
                objec.pec_finalizado = True

            if 'comodecirqueno_finalizado' in request.POST:
                objec.comodecirqueno_finalizado = True

            if 'comunicacion_finalizado' in request.POST:
                objec.comunicacion_finalizado = True

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