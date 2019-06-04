from django.contrib import admin

from .models import RodzajUbrania, Ubranie


@admin.register(RodzajUbrania)
class RodzajUbraniaAdmin(admin.ModelAdmin):
    pass

    
@admin.register(Ubranie)
class UbranieAdmin(admin.ModelAdmin):
    pass
