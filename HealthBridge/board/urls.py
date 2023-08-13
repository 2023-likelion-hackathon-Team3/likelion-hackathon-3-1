from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "board"

urlpatterns = [
    path("", views.board, name="board-main"),
    path("write/", views.write, name="board-write"),
    path("detail/<int:id>/", views.detail, name="board-detail"),
    path(
        "detail/<int:id>/update/<int:ansid>/", views.updateAnswer, name="answer-update"
    ),
    path(
        "detail/<int:id>/delete/<int:ansid>/", views.deleteAnswer, name="answer-delete"
    ),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
