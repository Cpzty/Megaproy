from django.urls import path
from .views import UserRecordView, ProfileRecordView

app_name = 'retos'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    path('profile', ProfileRecordView.as_view(), name='profiles')
]
