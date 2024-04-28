from django.urls import path

from .views import (
    home_view,
    JuegoListView,
    JuegoDetailView,
    JuegoDeleteView,
    JuegoUpdateView,
    JuegoCreateView,
)

urlpatterns = [
    path("", home_view),
    path("juego/list/", JuegoListView.as_view(), name="juego-list"),
    path("juego/create/", JuegoCreateView.as_view(), name="juego-create"),
    path("juego/<int:pk>/detail/", JuegoDetailView.as_view(), name="juego-detail"),
    path("juego/<int:pk>/update/", JuegoUpdateView.as_view(), name="juego-update"),
    path("juego/<int:pk>/delete/", JuegoDeleteView.as_view(), name="juego-delete"),
]
