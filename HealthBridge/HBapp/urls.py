from django.urls import path, include
from . import views

app_name = "HBapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("upload/", views.text_extraction, name="text_extraction"),
    path("add/", views.keyword_add, name="keyword_add"),
]
