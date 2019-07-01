from django.conf import settings
from django.db import models

from pracownicy.models import Pracownik


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        print('  ------ iter ------')
        pracownicy_ids = self.cart.keys()
        print('  keys: ', self.cart.keys())
        print('  values: ', self.cart.values())
        print('  items: ', self.cart.items())
        print('  type of cart: ', type(self.cart))
        pracownicy = Pracownik.objects.filter(id__in = pracownicy_ids)
        cart = self.cart.copy()
        for pracownik in pracownicy:
            cart[str(pracownik.id)] = pracownik
        for item in cart.values():
            yield item

    def add(self, pracownik_id, rodzaj_ubrania_id, quantity=1):
        pracownik_id = str(pracownik_id)
        rodzaj_ubrania_id = str(rodzaj_ubrania_id)
        if pracownik_id not in self.cart:
            self.cart[pracownik_id] = {}
        self.cart[pracownik_id][rodzaj_ubrania_id] = {
            'quantity' : quantity,
            }

        # if update_quantity:
        #    print('----------------- update quantitny     ')
        # else:
        #    self.cart[pracownik_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True
