from django.conf import settings

from odziez.ubrania.models import RodzajUbrania, Ubranie

class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save empty cart sessions
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Iterate over the items in the cart
        and get the products from database
        """
        product_ids = self.cart.keys()
        products = RodzajUbrania.objects.filter(id__in = product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

    def add(self, rodzaj_ubrania_id, pracownik_id, quantity = 1, update_quantity = False):
        rodzaj_ubrania_id = str(rodzaj_ubrania_id)
        if rodzaj_ubrania_id not in self.cart:
            self.cart[rodzaj_ubrania_id]['quantity'] = quantity
        else:
            self.cart[rodzaj_ubrania_id]['quantity'] += quantity
        self.save()

    def clear(self):
        """
        Remove cart from session.
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def remove(self, product):
        """
        Remove product from cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True
