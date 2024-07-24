from django.urls import path
from .views import LoginView, Users

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("users/", Users.as_view(), name="users"),
]
