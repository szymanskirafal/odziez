from django import forms

class CartAddUbranieForm(forms.Form):
    quantity = forms.IntegerField(
        initial = 0,
        min_value = 0,
        max_value = 1,
        )
    update = forms.BooleanField(
        required = False,
        initial = False,
        widget = forms.HiddenInput,
        )
