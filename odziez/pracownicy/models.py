from django.db import models


class Stanowisko(models.Model):
    PRACOWNIK = 'PR'
    KIEROWNIK = 'KI'
    RODZAJ_STANOWISKA = [
        (PRACOWNIK, 'Pracownik'),
        (KIEROWNIK, 'Kierownik'),
        ]
    rodzaj_stanowiska = models.CharField(
        max_length = 2,
        choices = RODZAJ_STANOWISKA,
        default = PRACOWNIK,
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


class Etat(models.Model):
    wielkosc_etatu = models.DecimalField(max_digits = 1, decimal_places = 2)
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

    class Meta:
        abstract = True


class Pracownik(models.Model):
    XL = 'XL'
    L = 'L'
    M = 'M'
    S = 'S'
    ROZMIAR = [
        (XL, 'XL'),
        (L, 'L'),
        (M, 'M'),
        (S, 'S'),]
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    imie = models.CharField(max_length = 15)
    nazwisko = models.CharField(max_length = 40)
	wzrost = models.PositiveSmallIntegerField(max_length = 3)
    kolnierzyk = models.PositiveSmallIntegerField(max_length = 2)
	szerokosc_w_pasie = models.PositiveSmallIntegerField(max_length = 3)
    rozmiar = models.CharField(max_length = 2, choices = ROZMIAR,)
	nr_buta = models.PositiveSmallIntegerField(max_length = 2)
    email = models.EmailField(blank = True)
    etat = models.ForeignKey(
        Etat,
        on_delete = models.CASCADE,
        related_name = 'pracownicy',
        )


class Nadzorca(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    imie = models.CharField(max_length = 15)
    nazwisko = models.CharField(max_length = 40)
    email = models.EmailField()
