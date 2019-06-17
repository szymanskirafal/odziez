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
        context['rodzaje_ubran'] = RodzajUbrania.objects.all()
        context['nowe_ubrania'] = self.get_rodzaje_ubran_niezamawianych_a_przyslugujacych()
        return context

    def get_stanowisko_pracownika(self):
        pracownik = self.get_object()
        stanowisko = pracownik.etat.stanowisko
        return stanowisko

    def get_rodzaje_ubran_zamawianych(self):
        ubrania_zamowione = Ubranie.objects.all().filter(pracownik = self.get_object())
        nazwy = []
        for ubranie in ubrania_zamowione:
            nazwy.append(ubranie.rodzaj.nazwa)
        return nazwy

    def get_rodzaje_ubran_przyslugujacych(self):
        rodzaje_ubran = RodzajUbrania.objects.all()
        przyslugujace_pracownikowi = rodzaje_ubran.filter(
            przysluguje = self.get_stanowisko_pracownika()
            )
        return przyslugujace_pracownikowi

    def get_rodzaje_ubran_niezamawianych_a_przyslugujacych(self):
        przyslugujace = self.get_rodzaje_ubran_przyslugujacych()
        niezamawiane_a_przyslugujace = przyslugujace.exclude(
            nazwa__in = self.get_rodzaje_ubran_zamawianych()
            )
        return niezamawiane_a_przyslugujace


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
        queryset = queryset.filter(etat__miejsce_pracy = self.get_miejsce_pracy())
        queryset = queryset.prefetch_related('ubrania')
        return queryset
