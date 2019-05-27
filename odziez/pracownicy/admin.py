from django.contrib import admin

from .models import Etat, MiejscePracy, Nadzorca, Pracownik, Stanowisko


@admin.register(Etat)
class EtatAdmin(admin.ModelAdmin):
    pass


@admin.register(MiejscePracy)
class MiejscePracyAdmin(admin.ModelAdmin):
    pass


@admin.register(Nadzorca)
class NadzorcaAdmin(admin.ModelAdmin):
    pass


@admin.register(Pracownik)
class PracownikAdmin(admin.ModelAdmin):
    pass

@admin.register(Stanowisko)
class StanowiskoAdmin(admin.ModelAdmin):
    pass
