from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from orders.models import Order

class SupervisorPassesTestMixin(UserPassesTestMixin):

    def test_func(self):
        try:
            test =  self.request.user.supervisor
        except ObjectDoesNotExist:
            test = False
        return test



class SupervisorOrderDetailView(
    LoginRequiredMixin,
    SupervisorPassesTestMixin,
    generic.DetailView,
    ):

    context_object_name = 'order'
    model = Order
    template_name = 'supervisor/order.html'


class SupervisorDashboardTemplateView(
    LoginRequiredMixin,
    SupervisorPassesTestMixin,
    generic.TemplateView,
    ):

    template_name = "supervisor/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.all()
        context['orders_not_approved'] = orders.filter(approved_by_supervisor = False)
        context['orders_sent_to_manufacturer'] = orders.filter(sent_to_manufacturer = True)
        context['orders_received_from_manufacturer'] = orders.filter(received_from_manufacturer = True)
        return context
