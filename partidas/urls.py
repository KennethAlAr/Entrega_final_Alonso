from django.urls import path

from .views import (
    home_view,
    JuegoListView,
    JuegoDetailView,
    JuegoDeleteView,
    JuegoUpdateView,
    JuegoCreateView,
    user_login_view,
    user_logout_view,
    UserUpdateView,
    user_creation_view,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("juego/list/", JuegoListView.as_view(), name="juego-list"),
    path("juego/create/", JuegoCreateView.as_view(), name="juego-create"),
    path("juego/<int:pk>/detail/", JuegoDetailView.as_view(), name="juego-detail"),
    path("juego/<int:pk>/update/", JuegoUpdateView.as_view(), name="juego-update"),
    path("juego/<int:pk>/delete/", JuegoDeleteView.as_view(), name="juego-delete"),
    path("login/", user_login_view, name='login'),
    path("logout/", user_logout_view, name='logout'),
    path("editar-perfil/", UserUpdateView.as_view(), name='editar-perfil'),
    path("crear-usuario/", user_creation_view, name='crear-usuario'),
]
