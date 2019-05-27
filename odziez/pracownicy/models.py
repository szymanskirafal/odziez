from django.db import models

from odziez.users.models import User


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True


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
    ulica_nr = models.CharField(max_length = 50)
    miejscowosc = models.CharField(max_length = 50)
    kod_pocztowy = models.CharField(max_length = 8)
    tel = models.CharField(max_length = 13)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Miejsca Pracy'

    def __str__(self):
        return self.nazwa + ' ' + self.miejscowosc


class Stanowisko(models.Model):
    nazwa = models.CharField(max_length = 150)
    opis = models.CharField(max_length = 300)

    class Meta:
        verbose_name_plural = 'Stanowiska'

    def __str__(self):
        return self.nazwa


class Etat(TimeStampedModel):
    miejsce_pracy = models.ForeignKey(
        MiejscePracy,
        on_delete = models.CASCADE,
        related_name = 'pracujacy_w_tym_miejscu',
        )
    stanowisko = models.ForeignKey(
        Stanowisko,
        on_delete = models.CASCADE,
        related_name = 'pracujacy_na_tym_stanowisku',
        )
    wielkosc_etatu = models.DecimalField(max_digits = 3, decimal_places = 2)

    class Meta:
        verbose_name_plural = 'Etaty'

    def __str__(self):
        etat = str(self.wielkosc_etatu)
        stanowisko = str(self.stanowisko)
        miejsce_pracy = str(self.miejsce_pracy)
        return etat + ' ' + stanowisko + ' ' + miejsce_pracy


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
        related_name = 'na_etacie',
        )

    class Meta:
        verbose_name_plural = 'Pracownicy'

    def __str__(self):
        return self.imie + self.nazwisko


class Kierownik(Osoba):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    email = models.EmailField()
    etat = models.ForeignKey(
        Etat,
        on_delete = models.CASCADE,
        related_name = 'kierownicy',
        )

    class Meta:
        verbose_name_plural = 'Kierownicy'

    def __str__(self):
        return self.imie + ' ' + self.nazwisko + ' ' + str(self.etat)


class Nadzorca(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    imie = models.CharField(max_length = 15)
    nazwisko = models.CharField(max_length = 40)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Nadzorcy'
