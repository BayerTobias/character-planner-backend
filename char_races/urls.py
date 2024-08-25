from django.urls import path
from .views import RaceListView

urlpatterns = [
    path("races/", RaceListView.as_view(), name="char-class"),
]
