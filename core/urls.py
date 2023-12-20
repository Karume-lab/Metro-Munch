from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("feedback/", views.feedback, name="feedback"),
    path("catering/", views.catering, name="catering"),
    path("login/", views.login, name="login")
]
