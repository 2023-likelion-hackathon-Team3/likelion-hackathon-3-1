from django.urls import path, include
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.postList, name='postList'),
    path('detail/<int:pk>', views.postDetail , name='postDetail'),
    path('update/<int:pk>', views.postUpdate , name='postUpdate'),
    path('delete/<int:pk>', views.postDelete, name='postDelete'),
    path('tag/<str:slug>', views.tag_page, name='tagPage'),
    
]