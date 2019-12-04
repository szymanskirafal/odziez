from django.core.mail import EmailMessage
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.utils.timezone import localdate
from django.views import generic

from clothes.models import Clothe, KindOfClothe
from employees.models import Employee, Manager, Supervisor

from .forms import OrderSendToSupervisorUpdateForm
from .models import Order


class OrdersChooseTemplateView(generic.TemplateView):
    template_name = "orders/choose.html"

    def get_order_during_composing(self):
        orders = Order.objects.all()
        orders = orders.filter(manager = self.request.user.manager.pk)
        try:
            order_during_composing = orders.get(during_composing = True)
        except ObjectDoesNotExist:
            order_during_composing = None
        return order_during_composing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_during_composing'] = self.get_order_during_composing()
        return context


class OrderNextOrSendTemplateView(generic.TemplateView):
    template_name = "orders/order-next-or-send.html"


class OrdersArchivedListView(generic.ListView):
    template_name = "orders/archived.html"


class OrdersPreparedTemplateView(generic.TemplateView):
    template_name = "orders/prepared.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        manager = Manager.objects.get(pk = self.request.user.manager.pk)
        orders = Order.objects.all().filter(manager = manager)
        order = orders.get(during_composing = True)
        context['order'] = order
        context['clothes'] = Clothe.objects.all().filter(order = order)
        return context


class OrderTemplateView(generic.TemplateView):
    template_name = "orders/redirect.html"

    def get_order_pk(self):
        manager = self.request.user.manager
        order, created = Order.objects.get_or_create(
            manager = manager,
            place_of_delivery = manager.work_place,
            during_composing = True,)
        return order.pk

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee_pk = self.kwargs['employee_pk']
        context['order'] = Order.objects.get(pk = self.get_order_pk())
        context['employee'] = Employee.objects.get(pk = employee_pk)
        context['kind'] = KindOfClothe.objects.get(pk = self.kwargs['kind_pk'])
        return context


class OrderSendUpdateView(generic.UpdateView):

    form_class = OrderSendToSupervisorUpdateForm
    model = Order
    success_url = reverse_lazy('employees:employees')
    template_name = "orders/send-to-supervisor.html"

    def form_valid(self, form):
        form.instance.during_composing = False
        form.instance.composed = True
        form.instance.sent_to_supervisor = True
        form.instance.date_of_sending_to_supervisor = localdate()
        supervisor = Supervisor.objects.first()
        email = EmailMessage(
            subject = 'Zamówienie odzieży roboczej',
            body = 'W aplikacji jest nowe zamówienie',
            to = [supervisor.email],
        )

        email.send()
        return super().form_valid(form)


class OrderSentToManufacturerListView(generic.ListView):

    context_object_name = 'orders'
    model = Order
    template_name = 'orders/sent-list.html'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        manager = Manager.objects.get(pk = self.request.user.manager.pk)
        orders = Order.objects.all().filter(manager = manager)
        orders = orders.filter(sent_to_manufacturer = True)
        return queryset

class OrderSentDetailView(generic.DetailView):
    context_object_name = 'order'
    model = Order
    template_name = 'orders/sent-detail.html'
