from .serializers import UserSerializer, ProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
#from django.template.loader import render_to_string
from django.urls import reverse

from django_rest_passwordreset.signals import reset_password_token_created
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
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
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        'Please use this token: {} at http://127.0.0.1:8000/api/password_reset/confirm/'.format(reset_password_token.key),
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
    #msg.attach_alternative(email_html_message, "text/html")
    msg.send()

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
        users = Profile.objects.filter(user=request.user)
        serializer = ProfileSerializer(users, many=True)
        return Response(serializer.data)

    def put(self, request):
        users = Profile.objects.filter(user=request.user)
        for objec in users:
            if 'racha' in request.POST:
                objec.racha += 1
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