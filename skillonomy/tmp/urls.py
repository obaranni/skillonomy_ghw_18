from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.index),
    path(r'explore_courses', views.explore_courses),
    path(r'profile', views.profile)
]
