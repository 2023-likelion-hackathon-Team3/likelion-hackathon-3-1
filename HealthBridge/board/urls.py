from django.urls import path, include
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.board, name='board-main'),
    path('create/', views.create, name='board-create'),
    path('detail/<int:id>/', views.detail, name='board-detail'),
    path('update/<int:id>/', views.update, name='board-update'),
]