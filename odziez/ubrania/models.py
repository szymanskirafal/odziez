from django.db import models

from pracownicy.models import Pracownik

class RodzajUbrania(models.Model):
    nazwa = models.CharField(max_length = 150, unique = True)
    opis = models.CharField(max_length = 300, blank = True)
    czasokres_wymiany = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'Rodzaje ubrań'

    def __str__(self):
        return self.nazwa + ' ' + 'wymiana co ' + str(self.czasokres_wymiany)

class Ubranie(models.Model):
    ubranie = models.ForeignKey(RodzajUbrania, on_delete = models.PROTECT)
    pracownik = models.OneToOneField(
        Pracownik,
        on_delete = models.CASCADE,
        related_name = 'ubrania',
        )
    zamowione = models.DateField(null = False, blank = True)
    otrzymane = models.DateField(null = True, blank = True)
    posiadane = models.DateField(null = True, blank = True)
    zniszczone = models.DateField(null = True, blank = True)

    class Meta:
        verbose_name_plural = 'Ubrania pracowników'

    def __str__(self):
        return str(self.ubranie) + ' ' + str(self.pracownik)
