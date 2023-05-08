from urllib import request
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, path

from main import views
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("bio/<int:id>", views.bio, name="bio"),
]
