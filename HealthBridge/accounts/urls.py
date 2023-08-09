from django.urls import path, include
from accounts import views
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    
]