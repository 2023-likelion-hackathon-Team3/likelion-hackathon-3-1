from django.urls import path, include
from . import views

app_name = "explain"

urlpatterns = [
    path("", views.explain, name="explain"),
]