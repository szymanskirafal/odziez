from django.contrib import admin

from .models import Zamowienie

@admin.register(Zamowienie)
class ZamowienieAdmin(admin.ModelAdmin):
    pass
