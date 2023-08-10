from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "mypage"

urlpatterns = [
    path("my/", views.my, name="my"),
    path("check/", views.check, name="check"),
    path("fix/", views.fix, name="fix"),
    path("add/tag/", views.addTag, name="addTag"),
    # path('delete/tag/', views.deleteTag, name='deleteTag'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
