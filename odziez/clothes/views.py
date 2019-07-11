from django.urls import reverse
from django.views import generic

from employees.models import Employee
from orders.models import Order

from .forms import ClotheCreateForm
from .models import Clothe, KindOfClothe


class KindsOfClothesListView(generic.ListView):
    model = KindOfClothe
    template_name = "clothes/kinds.html"

class ClotheCreateView(generic.CreateView):
    form_class = ClotheCreateForm
    model = Clothe
    success_url = '/'
    template_name = "clothes/clothe-create.html"

    def form_valid(self, form):
        print('   --- form valid called ')
        print('   --- kind_pk: ', self.kwargs['kind_pk'])
        form.instance.kind = KindOfClothe.objects.get(pk = self.kwargs['kind_pk'])
        form.instance.order = Order.objects.get(pk = self.kwargs['order_pk'])
        form.instance.employee = Employee.objects.get(pk = self.kwargs['employee_pk'])
        form.instance.prepared_to_order = True
        return super().form_valid(form)


#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['employee'] = Employee.objects.get(pk = self.kwargs['employee_pk'])
#        context['order'] = Order.objects.get(pk = self.kwargs['order_pk'])
#        return context

class KindTemplateView(generic.TemplateView):
    template_name = 'clothes/kind-template.html'
