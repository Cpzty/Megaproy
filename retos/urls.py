from django.urls import path
from .views import UserRecordView, ProfileRecordView, CuestionarioAEView, CuestionarioAERView, CuestionarioPECView, CuestionarioPECRView, CuestionarioNOView, CuestionarioNORView, CuestionarioComunicacionView,CuestionarioComunicacionRView, HistorialEmocionesView, RetoRecordView, CuestionariosView, PreguntasView, InsigniasView, RespuestasView, Insignias_usuarioView

app_name = 'retos'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    #path('<user>/profile/', ProfileUpView.as_view(), name='profiles')
    path('profile/', ProfileRecordView.as_view(), name='profiles'),
    path('auto_estima/', CuestionarioAEView.as_view(), name='auto_estima'),
    path('auto_estima_realizado/', CuestionarioAERView.as_view(), name='auto_estima_realizado'),
    path('pec/', CuestionarioPECView.as_view(), name='competencia_emocional'),
    path('pec_realizado/', CuestionarioPECRView.as_view(), name='competencia_emocional_realizado'),
    path('como_decir_que_no/', CuestionarioNOView.as_view(), name='cuestionario_no'),
    path('como_decir_que_no_realizado/', CuestionarioNORView.as_view(), name='cuestionario_no_realizado'),
    path('comunicacion_efectiva/', CuestionarioComunicacionView.as_view(), name='cuestionario_comunicacion_efectiva'),
    path('comunicacion_efectiva_realizado/', CuestionarioComunicacionRView.as_view(), name='cuestionario_comunicacion_efectiva_realizado'),
    path('historial_emociones/', HistorialEmocionesView.as_view(),name='historial_emociones'),
    path('reto_finalizado/', RetoRecordView.as_view(), name='reto_finalizado'),
    path('cuestionarios/', CuestionariosView.as_view(), name='cuestionarios'),
    path('preguntas/', PreguntasView.as_view(), name='preguntas'),
    path('insignias/', InsigniasView.as_view(), name='insignias'),
    path('respuestas/', RespuestasView.as_view(), name='respuestas'),
    path('insignias_usuario/', Insignias_usuarioView.as_view(), name='insignias_usuario'),

]
