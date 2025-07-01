from django.urls import path

from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("login", views.login, name="login"),
    path("project/new", views.new_project, name="project_new"),
]
