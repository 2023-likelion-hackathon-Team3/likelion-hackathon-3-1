from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "cameraapp"

urlpatterns = [
    path("", views.webcam_view, name="capture"),
    path("save_cropped_photo/", views.save_cropped_photo, name="save_cropped_photo"),
]
