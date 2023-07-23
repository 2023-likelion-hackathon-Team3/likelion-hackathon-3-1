from django.urls import path, include
from . import views

app_name = 'HBapp'

urlpatterns = [
    path('', views.index, name='index'),

]