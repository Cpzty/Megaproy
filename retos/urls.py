from django.urls import path
from .views import UserRecordView, ProfileRecordView, ProfileUpView, CuestionarioAEView, CuestionarioAERView, CuestionarioPECView, CuestionarioPECRView

app_name = 'retos'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    #path('<user>/profile/', ProfileUpView.as_view(), name='profiles')
    path('profile/', ProfileRecordView.as_view(), name='profiles'),
    path('auto_estima/', CuestionarioAEView.as_view(), name='auto_estima'),
    path('auto_estima_realizado/', CuestionarioAERView.as_view(), name='auto_estima_realizado'),
    path('pec', CuestionarioPECView.as_view(), name='competencia_emocional'),
    path('pec_realizado', CuestionarioPECRView.as_view(), name='competencia_emocional_realizado'),

]
