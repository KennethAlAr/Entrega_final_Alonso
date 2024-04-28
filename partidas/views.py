from django.urls import reverse_lazy
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.shortcuts import render, redirect

from .models import Juego, Reserva, Sistema

# Create your views here.

def home_view(request):
    return render(request, "partidas/home.html")

#CRUD JUEGOS

class JuegoListView(ListView):
    model = Juego
    template_name = "partidas/vbc/juego-list.html"
    context_object_name = "todos_los_juegos"

class JuegoDetailView(DetailView):
    model = Juego
    template_name = "partidas/vbc/juego-detail.html"
    context_object_name = "juego"

class JuegoDeleteView(DeleteView):
    model = Juego
    template_name = "partidas/vbc/juego-confirm-delete.html"
    success_url = reverse_lazy("juego-list")

class JuegoUpdateView(UpdateView):
    model = Juego
    template_name = "partidas/vbc/juego-form.html"
    fields = [
        "nombre",
        "disponible",
        "numero_de_jugadores",
        "sistema_de_juego",
        "descripcion",
        "fecha",
        "hora_inicio",
        "hora_fin"
        ]
    context_object_name = "juego"
    success_url = reverse_lazy("juego-list")

class JuegoCreateView(CreateView):
    model = Juego
    template_name = "partidas/vbc/juego-form.html"
    fields = ["nombre", "disponible", "numero_de_jugadores", "sistema_de_juego", "descripcion", "fecha", "hora_inicio", "hora_fin"]
    success_url = reverse_lazy("juego-list")

# Create 