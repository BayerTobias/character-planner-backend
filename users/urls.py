from django.urls import path
from .views import LoginView, Users, CheckAuth

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("users/", Users.as_view(), name="users"),
    path("check/", CheckAuth.as_view(), name="check"),
]
