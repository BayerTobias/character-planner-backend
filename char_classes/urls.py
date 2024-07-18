from django.urls import path
from .views import CharClassView

urlpatterns = [
    path("classes/", CharClassView.as_view(), name="char-class"),
]
