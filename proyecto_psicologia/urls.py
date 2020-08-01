"""proyecto_psicologia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.authtoken import views
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm, reset_password_validate_token
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('django_query_profiler/', include('django_query_profiler.client.urls')),
    path('admin/', admin.site.urls),
    path('retos/', include('retos.urls', namespace='retos')),
    path('retos-token-auth/', views.obtain_auth_token, name='retos-token-auth'),
    url(r'^api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    #path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    
    #path('accounts/', include('allauth.urls')),
    #path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    #path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
