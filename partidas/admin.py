from django.contrib import admin

from .models import Sistema, Juego, Reserva, Avatar

admin.site.register(Sistema)
admin.site.register(Juego)
admin.site.register(Reserva)
admin.site.register(Avatar)