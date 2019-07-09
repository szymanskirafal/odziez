from django.views import generic

from employees.models import Employee

from .models import KindOfClothe


class KindsOfClothesListView(generic.ListView):
    model = KindOfClothe
    template_name = "clothes/kinds.html"

class KindOfClotheDetailView(generic.edit.FormMixin, generic.DetailView):
    context_object_name = 'kind'
    model = KindOfClothe
    template_name = "clothes/kind.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee_pk = self.kwargs['employee_pk']
        context['employee'] = Employee.objects.get(pk = employee_pk)
        return context
