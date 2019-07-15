from django.db.models import Q
from django.utils.timezone import localdate
from django.views import generic

from clothes.models import KindOfClothe, Clothe

from .models import Employee


class EmployeeNewDetailView(generic.DetailView):
    context_object_name = 'employee'
    model = Employee
    template_name = 'employees/employee-new.html'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        #queryset = queryset.prefetch_related('clothes')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['never_ordered_but_available'] = self.get_never_ordered_but_available()
        context['can_be_ordered_again'] = self.get_can_be_ordered_again()
        context['kinds_can_be_ordered_again'] = self.get_kinds_can_be_ordered_again()
        context['prepared_to_order'] = self.get_prepared_to_order()
        context['rest_of_clothes'] = self.get_rest_of_clothes()
        return context

    def get_rest_of_clothes(self):
        
        return clothes

    def get_prepared_to_order(self):
        clothes = self.get_clothes_of_employee()
        clothes = clothes.filter(prepared_to_order = True)
        return clothes

    def get_kinds_of_ordered_but_not_prepared_to_order(self):
        return set(
            kind
            for kind in self.get_kinds_of_ordered()
            if kind not in self.get_kinds_of_prepared_to_order()
            )

    def get_clothes_ordered_but_not_prepared_to_order(self):
        print('  -- get_clothes_ordered_but_not_prepared_to_order  ')
        print('  -- clothes  ', self.get_ordered().exclude(prepared_to_order = True))
        return self.get_ordered().exclude(prepared_to_order = True)

    def get_firsts_of_clothes_ordered_but_not_prepared_to_order(self):
        clothes = self.get_clothes_ordered_but_not_prepared_to_order()
        print('  -- get_firsts_of_clothes_ordered_but_not_prepared_to_order  ')
        print('  -- clothes  ', clothes)
        kinds = self.get_kinds_of_ordered_but_not_prepared_to_order()
        return clothes.filter(kind__in = kinds)

    def get_can_be_ordered_again(self):
        clothes = self.get_firsts_of_clothes_ordered_but_not_prepared_to_order()
        print('  -- get_can_be_ordered_again  ')
        print('  -- clothes  ', clothes)
        return [
            clothe
            for clothe
            in clothes
            if clothe.can_be_ordered_again == True
            ]

    def get_kinds_can_be_ordered_again(self):
        return set(
            clothe.kind
            for clothe
            in self.get_can_be_ordered_again()
            )

    def get_kinds_of_ordered(self):
        return set(clothe.kind for clothe in self.get_ordered())

    def get_kinds_of_prepared_to_order(self):
        return set(clothe.kind for clothe in self.get_prepared_to_order())

    def get_position(self):
        employee = self.get_object()
        return employee.job.position

    def get_available(self):
        return KindOfClothe.objects.all().filter(
            available_for = self.get_position())

    def get_clothes_of_employee(self):

        print('  -- get_clothes_of_employee  ')
        # print('  -- clothes  ', Clothe.objects.all().filter(employee = self.object))
        # return Clothe.objects.all().filter(employee = self.object)
        return self.get_object().clothes

    def get_ordered(self):
        clothes = self.get_clothes_of_employee()
        print('  -- get ordered  --  ', clothes.filter(ordered__lte = localdate()))
        return clothes.filter(ordered__lte = localdate())

    def get_prepared_to_order(self):
        clothes = self.get_clothes_of_employee()
        return clothes.filter(prepared_to_order = True)

    def get_ordered_or_prepared_to_order(self):
        return self.get_ordered() | self.get_prepared_to_order()

    def get_names_of_available(self):
        return set(kind.name for kind in self.get_available())

    def get_names_of_ordered_or_prepared_to_order(self):
        return set(
            clothe.kind.name
            for clothe in self.get_ordered_or_prepared_to_order()
            )

    def get_names_of_never_ordered_but_available(self):
        return set(
            name
            for name in self.get_names_of_available()
            if name not in self.get_names_of_ordered_or_prepared_to_order()
            )

    def get_never_ordered_but_available(self):
        return KindOfClothe.objects.all().filter(
            name__in = self.get_names_of_never_ordered_but_available()
            )


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
