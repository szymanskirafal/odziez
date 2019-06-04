from django import forms

class CartAddUbranieForm(forms.Form):
    UBRANIE_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,5)]
    quantity = forms.TypedChoicedField(choice = UBRANIE_QUANTITY_CHOICES)
    update = forms.BooleanField(
        required = False,
        initial = False,
        widget = forms.HiddentInput,
        )
