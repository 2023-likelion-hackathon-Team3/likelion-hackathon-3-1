from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "HBapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("upload/", views.text_extraction, name="text_extraction"),
    path("add/", views.keyword_add, name="keyword_add"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
