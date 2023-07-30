from django.urls import path, include
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.board, name='board-main'),
    path('create/', views.write, name='board-write'),
    path('detail/<int:id>/', views.detail, name='board-detail'),
]