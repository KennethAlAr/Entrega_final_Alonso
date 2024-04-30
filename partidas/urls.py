from django.urls import path

from .views import (
    home_view,
    JuegoListView,
    JuegoDetailView,
    JuegoDeleteView,
    JuegoUpdateView,
    JuegoCreateView,
    juego_search_view,
    SistemaListView,
    SistemaDetailView,
    SistemaUpdateView,
    SistemaDeleteView,
    SistemaCreateView,
    sistema_search_view,
    ReservaListView,
    ReservaDetailView,
    ReservaUpdateView,
    ReservaDeleteView,
    ReservaCreateView,
    user_login_view,
    user_logout_view,
    UserUpdateView,
    user_creation_view,
    avatar_view,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("juego/list/", JuegoListView.as_view(), name="juego-list"),
    path("juego/create/", JuegoCreateView.as_view(), name="juego-create"),
    path("juego/<int:pk>/detail/", JuegoDetailView.as_view(), name="juego-detail"),
    path("juego/<int:pk>/update/", JuegoUpdateView.as_view(), name="juego-update"),
    path("juego/<int:pk>/delete/", JuegoDeleteView.as_view(), name="juego-delete"),
    path("juego/search/", juego_search_view, name="juego-search"),
    path("sistema/list/", SistemaListView.as_view(), name="sistema-list"),
    path("sistema/create/", SistemaCreateView.as_view(), name="sistema-create"),
    path("sistema/<int:pk>/detail/", SistemaDetailView.as_view(), name="sistema-detail"),
    path("sistema/<int:pk>/update/", SistemaUpdateView.as_view(), name="sistema-update"),
    path("sistema/<int:pk>/delete/", SistemaDeleteView.as_view(), name="sistema-delete"),
    path("sistema/search/", sistema_search_view, name="sistema-search"),
    path("reserva/list/", ReservaListView.as_view(), name="reserva-list"),
    path("reserva/create/", ReservaCreateView.as_view(), name="reserva-create"),
    path("reserva/<int:pk>/detail/", ReservaDetailView.as_view(), name="reserva-detail"),
    path("reserva/<int:pk>/update/", ReservaUpdateView.as_view(), name="reserva-update"),
    path("reserva/<int:pk>/delete/", ReservaDeleteView.as_view(), name="reserva-delete"),
    path("login/", user_login_view, name='login'),
    path("logout/", user_logout_view, name='logout'),
    path("editar-perfil/", UserUpdateView.as_view(), name='editar-perfil'),
    path("crear-usuario/", user_creation_view, name='crear-usuario'),
    path("avatar/add", avatar_view, name="avatar-add"),
]
