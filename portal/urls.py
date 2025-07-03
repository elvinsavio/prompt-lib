from django.urls import path

from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("login", views.login, name="login"),
    path("project/new", views.project_new, name="project_new"),
    path("library", views.library_view_all, name="library_all"),
    path("library/new", views.library_new, name="library_new"),
]
