from django.urls import path
from .views import UserRecordView, ProfileRecordView, HistorialEmocionesView, RetoRecordView, CuestionariosView, PreguntasView, InsigniasView, RespuestasView, Insignias_usuarioView, ComentariosView, FrasesView

app_name = 'retos'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    #path('<user>/profile/', ProfileUpView.as_view(), name='profiles')
    path('profile/', ProfileRecordView.as_view(), name='profiles'),
    path('historial_emociones/', HistorialEmocionesView.as_view(),name='historial_emociones'),
    path('reto_finalizado/', RetoRecordView.as_view(), name='reto_finalizado'),
    path('cuestionarios/', CuestionariosView.as_view(), name='cuestionarios'),
    path('preguntas/', PreguntasView.as_view(), name='preguntas'),
    path('insignias/', InsigniasView.as_view(), name='insignias'),
    path('respuestas/', RespuestasView.as_view(), name='respuestas'),
    path('insignias_usuario/', Insignias_usuarioView.as_view(), name='insignias_usuario'),
    path('comentarios/', ComentariosView.as_view(), name='comentarios'),
    path('frases/', FrasesView.as_view(), name='frases'),

]
