from django.conf import settings
from django.db import models

class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

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
