from django.urls import path, include
from doctor import views
from doctor.views import *

app_name = "doctor"

urlpatterns = [
    path("accounts/signup/", views.doctor_signup, name="doctor_signup"),
    path("accounts/login/", views.doctor_login, name="doctor_login"),
    path("accounts/select_hospital/", views.dropdown_view, name="select_hospital"),
    path("main/", views.doctor_main, name="doctor_main"),
    path("result/<int:id>/", views.doctor_result, name="doctor_result"),
    path("info/<int:id>/", views.map_view, name="doctor-info"),
    path("start/", views.doctor, name="doctor_start"),
]
