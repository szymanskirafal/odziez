from django.db import models
from django.urls import reverse

from odziez.users.models import User


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True


class WorkPlace(models.Model):
    STATION = 'ST'
    BASE = 'BA'
    TYPE_OF_WORKPLACE = [
        (STATION, 'Stacja Paliw'),
        (BASE, 'Baza Magazynowa'),
        ]
    rodzaj = models.CharField(
        max_length = 2,
        choices = TYPE_OF_WORKPLACE,
        default = STATION,
        )
    name = models.CharField(max_length = 150)
    street = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    postal_code = models.CharField(max_length = 8)
    phone = models.CharField(max_length = 13)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Miejsca Pracy'

    def __str__(self):
        return self.name + ' ' + self.city


class Position(models.Model):
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 300)

    class Meta:
        verbose_name_plural = 'Stanowiska'

    def __str__(self):
        return self.name


class Job(TimeStampedModel):
    work_place = models.ForeignKey(
        WorkPlace,
        on_delete = models.CASCADE,
        )
    position = models.ForeignKey(
        Position,
        on_delete = models.CASCADE,
        )
    size_of_job = models.DecimalField(max_digits = 3, decimal_places = 2)

    class Meta:
        verbose_name_plural = 'Etaty'

    def __str__(self):
        job = str(self.size_of_job)
        position = str(self.position)
        work_place = str(self.work_place)
        return 'etat - ' + job + '  ' + position + ' ' + work_place


class Person(TimeStampedModel):
    WOMAN = 'W'
    MAN = 'M'
    SEX = [
        (WOMAN, 'Kobieta'),
        (MAN, 'Mężczyzna'),
        ]
    XL = 'XL'
    L = 'L'
    M = 'M'
    S = 'S'
    SIZE = [
        (XL, 'XL'),
        (L, 'L'),
        (M, 'M'),
        (S, 'S'),
        ]
    sex = models.CharField(max_length = 1, choices = SEX,)
    name = models.CharField(max_length = 15)
    surname = models.CharField(max_length = 40)
    height = models.PositiveSmallIntegerField()
    colar = models.PositiveSmallIntegerField()
    width_waist = models.PositiveSmallIntegerField()
    body_size = models.CharField(max_length = 2, choices = SIZE,)
    shoe_size = models.PositiveSmallIntegerField()

    class Meta:
        abstract = True


class Employee(Person):
    job = models.ForeignKey(
        Job,
        on_delete = models.CASCADE,
        )

    class Meta:
        verbose_name_plural = 'Pracownicy'

    def __str__(self):
        return self.name + ' ' + self.surname  + ' ' + str(self.job)

    def get_absolut_url(self):
        return reverse('employees:employee', args=[str(self.id)])


class Manager(Person):
    job = models.ForeignKey(
        Job,
        on_delete = models.CASCADE,
        )
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Kierownicy'

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + str(self.job)


class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Nadzorcy'

    def __str__(self):
        return self.name
