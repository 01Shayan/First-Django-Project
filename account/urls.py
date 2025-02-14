from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("users/", views.getuser, name="get_user"),
    path("delete/<int:id_user>/", views.delete, name="delete"),
    path("profile/edit/<id_user>/", views.profile_edit, name="profile_edit"),
    path("users/edit/<id_user>/", views.user_edit, name="user_edit"),
    path("login/", views._login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views._logout, name="logout"),

    # todo
    path("password-reset/", views.password_reset, name="password_reset"),

    # test page
    path("test/", views.test, name="test"),
]
