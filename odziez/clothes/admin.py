from django.contrib import admin

from .models import KindOfClothe, Clothe


@admin.register(KindOfClothe)
class KindOfClotheAdmin(admin.ModelAdmin):
    pass


@admin.register(Clothe)
class ClotheAdmin(admin.ModelAdmin):
    pass
