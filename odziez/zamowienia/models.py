from django.db import models

from ubrania.models import Ubranie
from pracownicy.models import Kierownik, MiejscePracy


class Zamowienie(models.Model):
    ubranie_zamawiane = models.ForeignKey(
        Ubranie,
        related_name = 'zlozone_zamowienia',
        on_delete = models.CASCADE,
        )
    zamawiajacy = models.ForeignKey(
        Kierownik,
        related_name = 'zamawiajacy',
        on_delete = models.CASCADE,
        )
    miejsce_dostawy = models.ForeignKey(
        MiejscePracy,
        related_name = 'zamawiane_ubrania',
        on_delete = models.CASCADE,
        )
    data_zamowienia = models.DateField(null = False, blank = False)
    data_zatwierdzenia = models.DateField(null = True, blank = True)
    data_wyslania = models.DateField(null = True, blank = True)
    data_otrzymania = models.DateField(null = True, blank = True)

    class Meta:
        verbose_name_plural = 'Zamówienia'
