from django.views import generic

from cart.forms import CartAddUbranieForm

from pracownicy.models import Pracownik

from .models import RodzajUbrania


class RodzajUbraniaListView(generic.ListView):
    model = RodzajUbrania
    template_name = "ubrania/rodzaje.html"

class RodzajUbraniaDetailView(generic.edit.FormMixin, generic.DetailView):
    context_object_name = 'rodzaj'
    form_class = CartAddUbranieForm
    model = RodzajUbrania
    template_name = "ubrania/rodzaj.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pracownik_pk = self.kwargs['pracownik_pk']
        context['pracownik'] = Pracownik.objects.get(pk = pracownik_pk)
        return context
