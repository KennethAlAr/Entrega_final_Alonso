from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Dado(models.TextChoices):
    D6 = "d6", ("Dado D6")
    D8 = "d8", ("Dado D8")
    D10 = "d10", ("Dado D10")
    D12 = "d12", ("Dado D12")
    D20 = "d20", ("Dado D20")
    MULTIPLE = "multi", ("Diversos dados")

class Base(models.TextChoices):
    DND5E = "dnd5e", ("Dungeons & Dragons 5ª Edición")
    DND3E = "dnd3e", ("Dungeons & Dragons 3ª Edición")
    FF3E = "ff3e", ("Final Fantasy 3ª Edición")
    WHFANTASY = "whf", ("Warhammer Fantasy Roleplay")
    WH40K = "wh40k", ("Warhammer 40.000 Roleplay")
    MARVEL_MV_RPG = "marvel", ("Marvel Multiverse Role-Playing Game")
    PATHFINDER = "path", ("Pathfinder 2ª Edición")
    CTHULHU = "cthul", ("Call of Cthulhu")
    CINCO_ANILLOS = "5ring", ("La Leyenda de los Cinco Anillos")

class Sistema(models.Model):
    nombre = models.CharField(max_length=100)
    dado = models.CharField(
        max_length=6,
        choices=Dado.choices,
        default=Dado.D20
        )
    base = models.CharField(
        max_length=6,
        choices=Base.choices,
        default=Base.DND5E
        )
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.nombre}"

class Juego(models.Model):
    nombre = models.CharField(max_length=250)
    disponible = models.BooleanField(default=True)
    numero_de_jugadores = models.IntegerField()
    sistema_de_juego = models.ForeignKey(Sistema, on_delete=models.CASCADE, related_name='sistema_de_juego')
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(default=timezone.now)
    hora_inicio = models.TimeField(default=timezone.now)
    hora_fin = models.TimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre}"

class Reserva(models.Model):
    jugador = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, related_name='reservas')
    raza = models.CharField(max_length=50)
    clase = models.CharField(max_length=50)
    experiencia = models.BooleanField(default=True)
    descripcion = models.TextField(max_length=500)

    def get_experiencia_display(self):
        return "Si" if self.experiencia else "No"

    def __str__(self):
        return f"¡{self.jugador} se ha unido a {self.juego}!"