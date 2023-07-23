from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post_user/", views.post_user, name='post_user'),
    path("teste/", views.get_message, name='get_message')
]
