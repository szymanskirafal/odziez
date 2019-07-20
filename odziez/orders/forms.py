from django.forms import HiddenInput, ModelForm

from .models import Order


class OrderSendToSupervisorUpdateForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            'during_composing',
            'composed',
            'sent_to_supervisor',
            'date_of_sending_to_supervisor',
            ]
        widgets = {
            'during_composing': HiddenInput,
            'composed': HiddenInput,
            'sent_to_supervisor': HiddenInput,
            'date_of_sending_to_supervisor': HiddenInput,
        }
