from django.contrib import admin

from .models import Clothe, KindOfClothe, Manufacturer


@admin.register(KindOfClothe)
class KindOfClotheAdmin(admin.ModelAdmin):
    pass


@admin.register(Clothe)
class ClotheAdmin(admin.ModelAdmin):
    pass


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass
