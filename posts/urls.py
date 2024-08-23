from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.session, name="login"),
    path("logout/", views.delete_session, name="logout"),
    path("home/", views.home, name="home"),
]
