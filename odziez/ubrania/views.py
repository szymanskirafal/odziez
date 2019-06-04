from django.views import generic

from .models import RodzajUbrania


class RodzajUbraniaListView(generic.ListView):
    model = RodzajUbrania
    template_name = "ubrania/rodzaje.html"
