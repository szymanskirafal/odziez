from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy

from ubrania.models import RodzajUbrania, Ubranie


#from .cart import Cart
from .forms import CartAddUbranieForm
"""
@require_POST
def cart_add(request, rodzaj_ubrania_id, pracownik_id):
    cart = Cart(request)
    rodzaj_ubrania = get_object_or_404(RodzajUbrania, id = rodzaj_ubrania_id)
    pracownik = get_object_or_404(Pracownik, id = pracownik_id)
    form = CartAddUbranieFrom(request.POST)
    if form.is_valid():
        cart.add(rodzaj_ubrania, pracownik)
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
        else:
            print(' ---------    WTF  ')
