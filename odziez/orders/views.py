from django.views import generic

from clothes.models import KindOfClothe
from employees.models import Employee
from orders.models import Order


class OrderTemplateView(generic.TemplateView):
    template_name = "orders/redirect.html"

    def get_order_pk(self):
        print('  -------------- ')
        print('  calling get_order_pk ')
        print('  request user ', self.request.user)
        print('  request user class', self.request.user.__class__)
        for m in dir(self.request.user):
            print(m)
        print('  -------------- ')
        print('  has attr', hasattr(self.request.user, 'manager'))
        print('  manager', self.request.user.manager)
        print('  work_place', self.request.user.manager.job.work_place)
        manager = self.request.user.manager
        order, created = Order.objects.get_or_create(
            manager = manager,
            place_of_delivery = manager.job.work_place,
            during_composing = True,)
        print('  created or not: ', created)
        print('  order.pk : ', order.pk)
        return order.pk

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee_pk = self.kwargs['employee_pk']
        context['order'] = Order.objects.get(pk = self.get_order_pk())
        context['employee'] = Employee.objects.get(pk = employee_pk)
        context['kind'] = KindOfClothe.objects.get(pk = self.kwargs['kind_pk'])
        return context