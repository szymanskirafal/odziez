from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from orders.models import Order


class SupervisorDashboardTemplateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.TemplateView,
    ):

    template_name = "supervisor/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.all()
        return context

    def test_func(self):
        try:
            test =  self.request.user.supervisor
        except ObjectDoesNotExist:
            test = False
        return test
