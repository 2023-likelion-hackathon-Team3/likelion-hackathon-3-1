"""
URL configuration for HealthBridge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
    path("ocr/", include("HBapp.urls", namespace="HBapp")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("board/", include("board.urls", namespace="board")),
    path("mypage/", include("mypage.urls", namespace="mypage")),
    path("post/", include("Post.urls", namespace="post")),
    path("quiz/", include("Quiz.urls", namespace="quiz")),
    path("authaccounts/", include("allauth.urls")),
    path("camera/", include("cameraapp.urls", namespace="cameraapp")),
    path("doctor/", include("doctor.urls", namespace="doctor")),
    path("explain/", include("explain.urls", namespace="explain")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
