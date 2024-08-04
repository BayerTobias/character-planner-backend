from django.urls import path
from .views import CharactersView


urlpatterns = [
    path("characters/", CharactersView.as_view(), name="characters-list"),
    path(
        "characters/<int:character_id>/",
        CharactersView.as_view(),
        name="character-details",
    ),
]
