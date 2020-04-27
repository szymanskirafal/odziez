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
        return employees.prefetch_related('clothes')

    def get_employees_values(self):
        employees = Employee.objects.all()
        employees = employees.filter(work_place = self.get_work_place())
        #employees = employees.prefetch_related('clothes')
        return employees.values()

    def get_employees_with_prefetched(self):
        employees = Employee.objects.all()
        employees = employees.filter(work_place = self.get_work_place())
        employees = employees.prefetch_related('clothes')
        employees_with_prefetched = employees.values(
          'id',
          'name',
          'clothes__kind__name',
          'clothes__prepared_to_order',
          'clothes__ordered',
          'clothes__received',
          'clothes__delivered_ok',
        )
        print('--- ', type(employees_with_prefetched))
        for fetched_dict in employees_with_prefetched:
            for k,v in fetched_dict.items():
                if v == 'Adam':
                    print(' Mamy Adama')
                    print(' clothes__kind__name: ', fetched_dict['clothes__kind__name'])
                    print(' clothes__prepared_to_order: ', fetched_dict['clothes__prepared_to_order'])
                    print(' clothes__ordered: ', fetched_dict['clothes__ordered'])
                    print(' clothes__received: ', fetched_dict['clothes__received'])
                    print(' clothes__delivered_ok: ', fetched_dict['clothes__delivered_ok'])
        return employees_with_prefetched

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clothes'] = self.get_clothes()
        context['employees'] = self.get_employees()
        context['employees_values'] = self.get_employees_values()
        context['employees_with_prefetched'] = self.get_employees_with_prefetched()
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
