from django.db import models

from pracownicy.models import Pracownik, Stanowisko

class RodzajUbrania(models.Model):
    nazwa = models.CharField(max_length = 150, unique = True)
    opis = models.CharField(max_length = 300, blank = True)
    czasokres_wymiany = models.PositiveSmallIntegerField()
    przysluguje = models.ManyToManyField(Stanowisko)

    class Meta:
        verbose_name_plural = 'Rodzaje ubrań'

    def __str__(self):
        return self.nazwa + ' ' + 'wymiana co ' + str(self.czasokres_wymiany) + 'przysluguje '+ str(self.przysluguje)

class Ubranie(models.Model):
    rodzaj = models.ForeignKey(
        RodzajUbrania,
        on_delete = models.CASCADE,
        related_name = 'wybrane',)
    pracownik = models.ForeignKey(
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
        return str(self.rodzaj) + ' ' + str(self.pracownik)
