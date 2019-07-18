from django.views import generic

from clothes.models import Clothe, KindOfClothe
from employees.models import Employee, Manager
from orders.models import Order


class OrdersChooseTemplateView(generic.TemplateView):
    template_name = "orders/choose.html"


class OrderNextOrSendTemplateView(generic.TemplateView):
    template_name = "orders/order-next-or-send.html"


class OrdersArchivedListView(generic.ListView):
    template_name = "orders/archived.html"


class OrdersPreparedTemplateView(generic.TemplateView):
    template_name = "orders/prepared.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.user.manager.pk
        manager = Manager.objects.get(pk = pk)
        orders = Order.objects.all().filter(manager = manager)
        #.prefetch_related('clothes_ordered')
        order = orders.get(during_composing = True)
        #order = order.prefetch_related('clothes_ordered')
        #context['clothes'] = Clothe.objects.all().filter(order = order)
        #context['order'] = order
        clothes = Clothe.objects.all().filter(order = order)
        names = [
            clothe.kind.name
            for clothe
            in clothes
            ]
        context['names'] = names
        #context['clothes'] = clothes
        return context




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
