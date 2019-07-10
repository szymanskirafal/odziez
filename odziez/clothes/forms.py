from django.forms import HiddenInput, ModelForm

from .models import Clothe


class ClotheCreateForm(ModelForm):
    class Meta:
        model = Clothe
        fields = [
            'ordered',
            'received',
            'owned',
            'destroyed',
            ]
        widgets = {
            'ordered': HiddenInput,
            'received': HiddenInput,
            'owned': HiddenInput,
            'destroyed': HiddenInput,
        }
