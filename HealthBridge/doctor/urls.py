from django.urls import path, include
from doctor import views
from doctor.views import *

app_name = "doctor"

urlpatterns = [
    path("signup/", views.doctor_signup, name="doctor_signup"),
    path("select_hospital/", views.dropdown_view, name="select_hospital"),
]
