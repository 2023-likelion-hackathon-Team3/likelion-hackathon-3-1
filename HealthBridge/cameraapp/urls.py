from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "cameraapp"

urlpatterns = [
    path("", views.webcam_view, name="capture"),
    path("save_cropped_photo/", views.save_cropped_photo, name="save_cropped_photo"),
    path("crop/", views.crop, name="crop"),
    path("result/", views.text_extraction, name="result"),
    path("upload/", views.text_extraction1, name="upload"),
    path("webcam_capture/", views.save_webcam_photo, name="save_webcam_photo"),
    # path("webcam_view/", views.webcam_capture_view, name="webcam_view"),
    # path("captured_image/",views.captured_image_crop_view,name="captured_image_crop",),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
