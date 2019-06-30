from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy

from pracownicy.models import Pracownik
from ubrania.models import RodzajUbrania, Ubranie

from cart.models import Cart
from .forms import CartAddUbranieForm
"""

def cart_add(request, rodzaj_ubrania_id, pracownik_id):
    cart = Cart(request)
    rodzaj_ubrania = get_object_or_404(RodzajUbrania, id = rodzaj_ubrania_id)
    pracownik = get_object_or_404(Pracownik, id = pracownik_id)
    form = CartAddUbranieFrom(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            rodzaj_ubrania,
            pracownik,
            quantity = cd['quantity',
            update_quantity = cd['update_quantity'],
            )
    return redirect('/')


# Create your views here.
"""

class CartAddFormView(generic.FormView):
    form_class = CartAddUbranieForm
    success_url = reverse_lazy('pracownicy:pracownicy')
    template_name = "cart/add.html"

    def form_valid(self, form):
        print('  ---------   def form_vallid called  ')
        if form.is_valid():
            print('  --------  form is valid  ')
            cart = Cart(self.request)
            rodzaj_ubrania = get_object_or_404(RodzajUbrania, id = self.kwargs.get('rodzaj_pk'))
            pracownik = get_object_or_404(Pracownik, id = self.kwargs.get('pracownik_pk'))
            cd = form.cleaned_data
            print('  -----  got cleaned_data    ')
            cart.add(
                pracownik_id = pracownik.id,
                rodzaj_ubrania_id = rodzaj_ubrania.id,
                quantity = cd['quantity'],
                #update_quantity = cd['update_quantity'],
                )
            print('  ------ cart.add called   ')
        else:
            print(' ---------    WTF  ')

        return redirect('/')
