from .models import Juego, Reserva, Sistema, Avatar
from .forms import UserEditForm, JuegoSearchForm, SistemaSearchForm, AvatarCreateForm
from django import forms
from django.urls import reverse_lazy
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request):
    return render(request, "partidas/home.html")

#CRUD SISTEMAS

class SistemaListView(LoginRequiredMixin, ListView):
    model = Sistema
    template_name = "partidas/vbc/sistema-list.html"
    context_object_name = "todos_los_sistemas"

class SistemaDetailView(LoginRequiredMixin, DetailView):
    model = Sistema
    template_name = "partidas/vbc/sistema-detail.html"
    context_object_name = "sistema"

class SistemaDeleteView(LoginRequiredMixin, DeleteView):
    model = Sistema
    template_name = "partidas/vbc/sistema-confirm-delete.html"
    success_url = reverse_lazy("sistema-list")

class SistemaUpdateView(LoginRequiredMixin, UpdateView):
    model = Sistema
    template_name = "partidas/vbc/sistema-form.html"
    fields = [
        "nombre",
        "dado",
        "base",
        "descripcion"
        ]
    context_object_name = "sistema"
    success_url = reverse_lazy("sistema-list")

class SistemaCreateView(LoginRequiredMixin, CreateView):
    model = Sistema
    template_name = "partidas/vbc/sistema-form.html"
    fields = [
        "nombre",
        "dado",
        "base",
        "descripcion"
        ] 
    success_url = reverse_lazy("sistema-list")

@login_required
def sistema_search_view(request):
    if request.method == "GET":
        form = SistemaSearchForm()
        return render(request, "partidas/vbc/sistema-form-search.html", context={"search_form": form})
    elif request.method == "POST":
        form = SistemaSearchForm(request.POST)
        if form.is_valid():
            nombre_de_sistema = form.cleaned_data["nombre"]
            sistemas_encontrados = Sistema.objects.filter(nombre=nombre_de_sistema).all()
            contexto = {"todos_los_sistemas": sistemas_encontrados}
            return render(request, "partidas/vbc/sistema-list.html", contexto)
        else:
            return render(request, "partidas/vbc/sistema-form-search.html", context={"search_form": form})

#CRUD JUEGOS

class JuegoListView(LoginRequiredMixin, ListView):
    model = Juego
    template_name = "partidas/vbc/juego-list.html"
    context_object_name = "todos_los_juegos"

class JuegoDetailView(LoginRequiredMixin, DetailView):
    model = Juego
    template_name = "partidas/vbc/juego-detail.html"
    context_object_name = "juego"

class JuegoDeleteView(LoginRequiredMixin, DeleteView):
    model = Juego
    template_name = "partidas/vbc/juego-confirm-delete.html"
    success_url = reverse_lazy("juego-list")

class JuegoUpdateView(LoginRequiredMixin, UpdateView):
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
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['fecha'].widget = forms.DateInput(attrs={'type': 'date'})
        form.fields['hora_inicio'].widget = forms.TimeInput(attrs={'type': 'time', 'step': 60})
        form.fields['hora_fin'].widget = forms.TimeInput(attrs={'type': 'time', 'step': 60})
        return form

    context_object_name = "juego"
    success_url = reverse_lazy("juego-list")

class JuegoCreateView(LoginRequiredMixin, CreateView):
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
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['fecha'].widget = forms.DateInput(attrs={'type': 'date'})
        form.fields['hora_inicio'].widget = forms.TimeInput(attrs={'type': 'time', 'step': 60})
        form.fields['hora_fin'].widget = forms.TimeInput(attrs={'type': 'time', 'step': 60})
        return form
    
    success_url = reverse_lazy("juego-list")

@login_required
def juego_search_view(request):
    if request.method == "GET":
        form = JuegoSearchForm()
        return render(request, "partidas/vbc/juego-form-search.html", context={"search_form": form})
    elif request.method == "POST":
        form = JuegoSearchForm(request.POST)
        if form.is_valid():
            nombre_de_juego = form.cleaned_data["nombre"]
            juegos_encontrados = Juego.objects.filter(nombre=nombre_de_juego).all()
            contexto = {"todos_los_juegos": juegos_encontrados}
            return render(request, "partidas/vbc/juego-list.html", contexto)
        else:
            return render(request, "partidas/vbc/juego-form-search.html", context={"search_form": form})
        
#CRUD RESERVAS

class ReservaListView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = "partidas/vbc/reserva-list.html"
    context_object_name = "todas_las_reservas"

    def get_queryset(self):
        return Reserva.objects.filter(jugador=self.request.user)

class ReservaDetailView(LoginRequiredMixin, DetailView):
    model = Reserva
    template_name = "partidas/vbc/reserva-detail.html"
    context_object_name = "reserva"

class ReservaDeleteView(LoginRequiredMixin, DeleteView):
    model = Reserva
    template_name = "partidas/vbc/reserva-confirm-delete.html"
    success_url = reverse_lazy("reserva-list")

class ReservaUpdateView(LoginRequiredMixin, UpdateView):
    model = Reserva
    template_name = "partidas/vbc/reserva-form.html"
    fields = [
        "juego",
        "raza",
        "clase",
        "experiencia",
        "descripcion",
        ]
    context_object_name = "reserva"
    success_url = reverse_lazy("reserva-list")

    def form_valid(self, form):
        form.instance.jugador = self.request.user
        return super().form_valid(form)

class ReservaCreateView(LoginRequiredMixin, CreateView):
    model = Reserva
    template_name = "partidas/vbc/reserva-form.html"
    fields = [
        "juego",
        "raza",
        "clase",
        "experiencia",
        "descripcion",
        ]
    success_url = reverse_lazy("reserva-list")

    def form_valid(self, form):
        form.instance.jugador = self.request.user
        return super().form_valid(form)

# login / logout / Editar usuario / Crear Usuario

def user_login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.user_cache
            if user is not None:
                login(request, user)
                return redirect("home")
    
    return render(request, "partidas/login.html", {"ingresar": form})

def user_logout_view(request):
    logout(request)
    return redirect("login")

class UserUpdateView(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = "partidas/user-edit-form.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user

def user_creation_view(request):
    if request.method == "GET":
        form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    
    return render(request, "partidas/crear-usuario.html", {"form": form})

# Avatar para usuario

def avatar_view(request):
    if request.method == "GET":
        contexto = {"avatar": AvatarCreateForm()}
    else:
        form = AvatarCreateForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]
            avatar_existente = Avatar.objects.filter(user=request.user)
            avatar_existente.delete()
            nuevo_avatar = Avatar(image=image, user=request.user)
            nuevo_avatar.save()
            return redirect("home")
        else:
            contexto = {"avatar": form}

    return render(request, "partidas/avatar-create.html", context=contexto)