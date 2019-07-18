from django.urls import path

from . import views

app_name = "orders"
urlpatterns = [
    path(
        "",
        view=views.OrderNextOrSendTemplateView.as_view(),
        name="order-next-or-send",
    ),
    path(
        "redirect/<int:kind_pk>/<int:employee_pk>/",
        view=views.OrderTemplateView.as_view(),
        name="redirect",
    ),
    path(
        "choose/",
        view=views.OrdersChooseTemplateView.as_view(),
        name="choose",
    ),
    path(
        "prepared/",
        view=views.OrdersPreparedTemplateView.as_view(),
        name="prepared",
    ),
    path(
        "archived/",
        view=views.OrdersArchivedListView.as_view(),
        name="archived",
    ),

]
