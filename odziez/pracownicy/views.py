from django.views import generic

from ubrania.models import RodzajUbrania, Ubranie

from .models import Pracownik

class PracownikDetailView(generic.DetailView):
    context_object_name = 'pracownik'
    model = Pracownik
    template_name = 'pracownicy/pracownik.html'

    



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
        context['ubrania_przyslugujace'] = RodzajUbrania.objects.all()
        return context

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        queryset = queryset.filter(etat__miejsce_pracy = self.get_miejsce_pracy())
        queryset = queryset.prefetch_related('ubrania')
        self.get_rodzaje_ubran_niezamawianych_a_dostepnych()
        return queryset

    def get_rodzaje_ubran_niezamawianych_a_dostepnych(self):
        wszytskie_rodzaje_ubran = RodzajUbrania.objects.all()
        zbior_nazw_wszystkich_rodzajow_ubran = set()
        for rodzaj in wszytskie_rodzaje_ubran:
            zbior_nazw_wszystkich_rodzajow_ubran.add(rodzaj.nazwa)
        zbior_nazw_ubran_zamawianych = set()
        wszystkie_ubrania_zamowione = Ubranie.objects.all()
        for ubranie in wszystkie_ubrania_zamowione:
            zbior_nazw_ubran_zamawianych.add(ubranie.ubranie.nazwa)
        print('------------')
        print(' wszystkie rodzaje ', zbior_nazw_wszystkich_rodzajow_ubran)
        print('------------')
        print(' zamawiane ', zbior_nazw_ubran_zamawianych)
        diff = zbior_nazw_wszystkich_rodzajow_ubran.difference(zbior_nazw_ubran_zamawianych)
        print('------------')
        print(' diff ', diff)
