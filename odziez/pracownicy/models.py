from django.db import models

from odziez.users.models import User


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True


class Stanowisko(models.Model):
    SPRZEDAWCA = 'SPRZ'
    PODJAZDOWY = 'PODJ'
    KIEROWNIK = 'KIER'
    RODZAJ_STANOWISKA = [
        (SPRZEDAWCA, 'Sprzedawca'),
        (PODJAZDOWY, 'Podjazdowy'),
        (KIEROWNIK, 'Kierownik'),
        ]
    rodzaj_stanowiska = models.CharField(
        max_length = 2,
        choices = RODZAJ_STANOWISKA,
        default = SPRZEDAWCA,
        )
    czasokres_wymiany = models.PositiveSmallIntegerField()


class MiejscePracy(models.Model):
    STACJA = 'ST'
    BAZA = 'BA'
    RODZAJ_MIEJSCA_PRACY = [
        (STACJA, 'Stacja Paliw'),
        (BAZA, 'Baza Magazynowa'),
        ]
    rodzaj = models.CharField(
        max_length = 2,
        choices = RODZAJ_MIEJSCA_PRACY,
        default = STACJA,
        )
    nazwa = models.CharField(max_length = 150)
    ul_i_nr = models.CharField(max_length = 50)
    kod_pocztowy = models.CharField(max_length = 8)
    miejscowosc = models.CharField(max_length = 50)
    tel = models.CharField(max_length = 13)
    email = models.EmailField()
"""

class Etat(TimeStampedModel):
    wielkosc_etatu = models.DecimalField(max_digits = 3, decimal_places = 2)
    stanowisko = models.ForeignKey(
        Stanowisko,
        on_delete = models.CASCADE,
        related_name = 'pracownicy',
        )
    miejsce_pracy = models.ForeignKey(
        MiejscePracy,
        on_delete = models.CASCADE,
        related_name = 'pracownicy',
        )


class Osoba(TimeStampedModel):
    KOBIETA = 'K'
    MEZCZYZNA = 'M'
    PLEC = [
        (KOBIETA, 'Kobieta'),
        (MEZCZYZNA, 'Mężczyzna'),
        ]
    XL = 'XL'
    L = 'L'
    M = 'M'
    S = 'S'
    ROZMIAR = [
        (XL, 'XL'),
        (L, 'L'),
        (M, 'M'),
        (S, 'S'),
        ]
    plec = models.CharField(max_length = 1, choices = PLEC,)
    imie = models.CharField(max_length = 15)
    nazwisko = models.CharField(max_length = 40)
    wzrost = models.PositiveSmallIntegerField()
    kolnierzyk = models.PositiveSmallIntegerField()
    szerokosc_w_pasie = models.PositiveSmallIntegerField()
    rozmiar = models.CharField(max_length = 2, choices = ROZMIAR,)
    nr_buta = models.PositiveSmallIntegerField()

    class Meta:
        abstract = True


class Pracownik(Osoba):
    etat = models.ForeignKey(
        Etat,
        on_delete = models.CASCADE,
        related_name = 'pracownicy',
        )


class Kierownik(Osoba):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    email = models.EmailField()
    etat = models.ForeignKey(
        Etat,
        on_delete = models.CASCADE,
        related_name = 'pracownicy',
        )
"""

class Nadzorca(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    imie = models.CharField(max_length = 15)
    nazwisko = models.CharField(max_length = 40)
    email = models.EmailField()
