from django.urls import path
from .views import UserRecordView, ProfileRecordView, ProfileUpView

app_name = 'retos'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    #path('<user>/profile/', ProfileUpView.as_view(), name='profiles')
    path('profile/', ProfileRecordView.as_view(), name='profiles')
]
