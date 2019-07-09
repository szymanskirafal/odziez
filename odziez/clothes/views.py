from django.views import generic

from employees.models import Employee
from orders.models import Order

from .models import Clothe, KindOfClothe


class KindsOfClothesListView(generic.ListView):
    model = KindOfClothe
    template_name = "clothes/kinds.html"

class ClotheCreateView(generic.CreateView):
    model = Clothe


#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['employee'] = Employee.objects.get(pk = self.kwargs['employee_pk'])
#        context['order'] = Order.objects.get(pk = self.kwargs['order_pk'])
#        return context

class KindTemplateView(generic.TemplateView):
    template_name = 'clothes/kind-template.html'
