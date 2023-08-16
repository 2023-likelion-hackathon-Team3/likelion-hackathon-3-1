from django.urls import path, include
from accounts import views
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('kakao/set_password/', views.set_password, name='set_password'),
    path('logout/', views.logout, name='logout'),
    path('start/', views.start, name='start'),
]