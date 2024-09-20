from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.session, name="login"),
    path("logout/", views.delete_session, name="logout"),
    path("home/", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("tasks/create/", views.create_task, name="create"),
    path("profile/edit", views.edit_profile, name="edit_profile"),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("like-task/<int:task_id>/", views.like_task, name="like_task"),
    path("task/<int:task_id>/", views.task_detail, name="task_detail"),
    path("task/<int:task_id>/add_comment/", views.add_comment, name="add_comment"),
    path("edit_comment/<int:comment_id>/", views.edit_comment, name="edit_comment"),
]
