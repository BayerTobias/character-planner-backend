from django.urls import path
from .views import CharClassView, CharClassDetailsView

urlpatterns = [
    path("classes/", CharClassView.as_view(), name="char-class"),
    path(
        "classes/<int:id>/", CharClassDetailsView.as_view(), name="char-class-details"
    ),
]
