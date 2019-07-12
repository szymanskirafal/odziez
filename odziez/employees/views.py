from django.db.models import Q
from django.utils.timezone import localdate
from django.views import generic

from clothes.models import KindOfClothe, Clothe

from .models import Employee


class EmployeeNewDetailView(generic.DetailView):
    context_object_name = 'employee'
    model = Employee
    template_name = 'employees/employee-new.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['never_ordered_but_available'] = self.get_never_ordered_but_available()
        return context

    def get_position(self):
        employee = self.get_object()
        return employee.job.position

    def get_available(self):
        return KindOfClothe.objects.all().filter(available_for = self.get_position())

    def get_ordered_or_prepared_to_order(self):
        clothes = Clothe.objects.all()
        clothes = clothes.filter(employee = self.object)
        ordered_or_prepared_to_order = clothes.filter(Q(ordered__lte = localdate()) | Q(prepared_to_order = True))
        return ordered_or_prepared_to_order

    def get_names_of_available(self):
        return set([kind.name for kind in self.get_available()])

    def get_names_of_ordered_or_prepared_to_order(self):
        return set([clothe.kind.name for clothe in self.get_ordered_or_prepared_to_order()])

    # def get_never_ordered_but_available(self):
    #    never_ordered_but_available = [
    #        name
    #        for name in self.get_names_of_available()
    #        if name not in self.get_names_of_ordered_or_prepared_to_order()
    #        ]

    #    never_ordered_but_available = KindOfClothe.objects.all().filter(
    #        name__in = never_ordered_but_available
    #        )

    #    return never_ordered_but_available




class EmployeeDetailView(generic.DetailView):
    context_object_name = 'employee'
    model = Employee
    template_name = 'employees/employee.html'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        queryset = queryset.prefetch_related('clothes')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['names_of_kinds_of_clothes_ordered'] = self.get_names_of_kinds_of_clothes_ordered()
        context['kinds_of_available_clothes'] = self.get_kinds_of_available_clothes()
        context['first_clothes'] = self.get_first_clothes()
        return context

    def get_position(self):
        employee = self.get_object()
        position = employee.job.position
        return position

    def get_first_clothes(self):
        clothes = self.get_clothes_ordered()
        kinds = self.get_kinds_of_available_clothes()
        first_clothes = []
        for kind in kinds:
            clothes_filtered = clothes.filter(kind = kind)
            first = clothes_filtered.first()
            first_clothes.append(first)
        return first_clothes

    def get_clothes_ordered(self):
        clothes = Clothe.objects.all()
        clothes_ordered = clothes.filter(employee = self.get_object())
        return clothes_ordered

    def get_names_of_kinds_of_clothes_ordered(self):
        names_of_kinds_of_clothes_ordered = []
        clothes_ordered = self.get_clothes_ordered()
        for clothe in clothes_ordered:
            names_of_kinds_of_clothes_ordered.append(clothe.kind.name)
            # [clothe.kind.name for clothe in self.get_clothes_ordered()]
        return names_of_kinds_of_clothes_ordered

    def get_kinds_of_clothes(self):
        kinds_of_clothes = KindOfClothe.objects.all()
        return kinds_of_clothes

    def get_kinds_of_available_clothes(self):
        kinds_of_clothes = self.get_kinds_of_clothes()
        kinds_of_available_clothes = kinds_of_clothes.filter(
            available_for = self.get_position()
            )
        return kinds_of_available_clothes


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
