from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from clothes.models import Clothe
from employees.models import Employee
from orders.models import Order

class SupervisorPassesTestMixin(UserPassesTestMixin):

    def test_func(self):
        try:
            test =  self.request.user.supervisor
        except ObjectDoesNotExist:
            test = False
        return test

class SupervisorClotheDeleteView(generic.DeleteView):
    context_object_name = 'clothe'
    model = Clothe
    template_name = "clothes/delete.html"
    success_url = reverse_lazy('supervisor:dashboard')


class SupervisorOrderDetailView(
    LoginRequiredMixin,
    SupervisorPassesTestMixin,
    generic.DetailView,
    ):

    context_object_name = 'order'
    model = Order
    template_name = 'supervisor/order.html'

    def get_clothes(self):
        clothes = Clothe.objects.all()
        clothes = clothes.filter(order = self.get_object())
        clothes = clothes.select_related('employee', 'kind', )
        clothes = clothes.values(
            'employee__id',
            'employee__name',
            'employee__surname',
            'kind__name',
            )
        return clothes

    def get_employees(self):
        employees = Employee.objects.all()
        employees = employees.filter(work_place = self.get_work_place())
        employees = employees.prefetch_related('clothes')
        return employees

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clothes'] = self.get_clothes()
        context['employees'] = self.get_employees()
        return context

    def get_work_place(self):
        return self.get_object().place_of_delivery


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
