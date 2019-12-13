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
        try:
            order_during_composing = self.orders.get(during_composing = True)
        except ObjectDoesNotExist:
            order_during_composing = None
        return order_during_composing

    def get_orders_sent_to_supervisor_not_approved_yet(self):
        orders = self.orders.filter(sent_to_supervisor = True)
        orders = orders.filter(approved_by_supervisor = False)
        return orders

    def get_orders_waiting_for_delivery(self):
        return self.orders.filter(sent_to_manufacturer = True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.set_orders_for_current_manager()
        context['order_during_composing'] = self.get_order_during_composing()
        context['orders_sent_to_supervisor'] = self.get_orders_sent_to_supervisor()
        context['orders_waiting_for_delivery'] = self.get_orders_waiting_for_delivery()
        return context

    def set_orders_for_current_manager(self):
        orders = Order.objects.all()
        orders = orders.filter(manager = self.request.user.manager.pk)
        return self.orders = orders


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
