from django.urls import path
from .views import UserRecordView, ProfileRecordView, ProfileUpView, CuestionarioAEView, CuestionarioAERView, CuestionarioPECView, CuestionarioPECRView, CuestionarioNOView, CuestionarioNORView

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

]
