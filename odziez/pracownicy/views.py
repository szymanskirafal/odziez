from django.views import generic

from .models import Pracownik


class PracownicyListView(generic.ListView):
    context_object_name = 'pracownicy'
    model = Pracownik
    template_name = "pracownicy/pracownicy.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books - Book.objects.all()
        context['miejsce_pracy'] = self.request.user.kierownik.etat.miejsce_pracy
        # context['imie'] = kierownik.imie
        # context['miejsce_pracy'] = kierownik.etat.miejsce_pracy
        return context

    def get_queryset(self):
        #kierownik = self.request.user
        #miejsce_pracy = MiejscePracy.objects.all().filter()
        miejsce_pracy = self.request.user.kierownik.etat.miejsce_pracy
        queryset = Pracownik.objects.all().filter(etat__miejsce_pracy = miejsce_pracy)
        return queryset
