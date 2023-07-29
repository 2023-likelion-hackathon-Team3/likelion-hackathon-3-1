from django.urls import path, include
from . import views

app_name = 'mypage'

urlpatterns = [
    path('my/', views.my , name='my'),
    path('check/', views.check , name='check'),
    path('fix/', views.fix , name='fix'),
    
]