from django.views import generic

from ubrania.models import RodzajUbrania, Ubranie

from .models import Pracownik


class PracownikDetailView(generic.DetailView):
    context_object_name = 'pracownik'
    model = Pracownik
    template_name = 'pracownicy/pracownik.html'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        queryset = queryset.prefetch_related('ubrania')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nazwy_ubran_zamawianych'] = self.get_nazwy_rodzajow_ubran_zamawianych
        context['rodzaje_ubran_przyslugujacych'] = self.get_rodzaje_ubran_przyslugujacych()
        return context

    def get_stanowisko_pracownika(self):
        pracownik = self.get_object()
        stanowisko = pracownik.etat.stanowisko
        return stanowisko

    def get_ubrania_zamowione(self):
        ubrania = Ubranie.objects.all()
        ubrania_zamowione = ubrania.filter(pracownik = self.get_object())
        return ubrania_zamowione

    def get_nazwy_rodzajow_ubran_zamawianych(self):
        nazwy_rodzajow_ubran_zamawianych = []
        ubrania_zamowione = self.get_ubrania_zamowione()
        for ubranie in ubrania_zamowione:
            nazwy_rodzajow_ubran_zamawianych.append(ubranie.rodzaj.nazwa)
        return nazwy_rodzajow_ubran_zamawianych

    def get_rodzaje_ubran(self):
        rodzaje_ubran = RodzajUbrania.objects.all()
        return rodzaje_ubran

    def get_rodzaje_ubran_przyslugujacych(self):
        rodzaje_ubran = self.get_rodzaje_ubran()
        rodzaje_ubran_przyslugujacych = rodzaje_ubran.filter(
            przysluguje = self.get_stanowisko_pracownika()
            )
        return rodzaje_ubran_przyslugujacych


class PracownicyListView(generic.ListView):
    context_object_name = 'pracownicy'
    miejsce_pracy = None
    model = Pracownik
    template_name = 'pracownicy/pracownicy.html'

    def get_miejsce_pracy(self):
        if self.miejsce_pracy:
            return self.miejsce_pracy
        else:
            self.miejsce_pracy = self.request.user.kierownik.etat.miejsce_pracy
            return self.miejsce_pracy

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['miejsce_pracy'] = self.get_miejsce_pracy()
        return context

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        queryset = queryset.filter(
            etat__miejsce_pracy = self.get_miejsce_pracy()
            )
        queryset = queryset.prefetch_related('ubrania')
        return queryset
