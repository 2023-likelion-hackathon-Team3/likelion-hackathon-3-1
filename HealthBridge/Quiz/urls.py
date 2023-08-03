from django.urls import path, include
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.quiz, name='quiz'),
    path('answer/<int:quiz_id>/', views.answer, name='answer'),
    path('search/',views.searchView,name="search"),
]