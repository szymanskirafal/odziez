from django.db.models import Q
from django.utils.timezone import localdate
from django.views import generic

from clothes.models import KindOfClothe, Clothe

from .models import Employee

class EmployeeDetailView(generic.DetailView):
    context_object_name = 'employee'
    model = Employee
    template_name = 'employees/employee.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kinds_that_can_be_ordered'] = self.get_kinds_that_can_be_ordered()
        return context

    def get_kinds_not_ordered_yet_but_availalble(self):

        kinds_available = KindOfClothe.objects.all().filter(
            available_for = self.object.job.position)

        clothes_ordered = Clothe.objects.all().filter(employee = self.object)

        kinds_ordered = set(
            clothe.kind
            for clothe
            in clothes_ordered
            )

        return set(
            kind
            for kind
            in kinds_available
            if kind not in kinds_ordered
            )

    def get_kinds_that_can_be_ordered_again_but_not_prepared_to_order(self):
        clothes = self.object.clothes
        clothes = clothes.filter(prepared_to_order = False)
        return set(
            clothe.kind
            for clothe
            in clothes
            if clothe.can_be_ordered_again == True
            )

    def get_kinds_that_can_be_ordered(self):
        kinds = set(
            kind
            for kind
            in (self.get_kinds_that_can_be_ordered_again_but_not_prepared_to_order() | self.get_kinds_not_ordered_yet_but_availalble())
            )
        return kinds


class EmployeesListView(generic.ListView):
    context_object_name = 'employees'
    work_place = None
    model = Employee
    template_name = 'employees/employees.html'

    def get_work_place(self):
        if self.work_place:
            return self.work_place
        else:
            self.work_place = self.request.user.manager.job.work_place
            return self.work_place

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['work_place'] = self.get_work_place()
        return context

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        queryset = queryset.filter(
            job__work_place = self.get_work_place()
            )
        queryset = queryset.prefetch_related('clothes')
        return queryset
