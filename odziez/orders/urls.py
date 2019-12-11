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
    path(
        "send/<int:pk>/",
        view=views.OrderSendUpdateView.as_view(),
        name="send",
    ),
    path(
        "sent/",
        view=views.OrderSentToManufacturerListView.as_view(),
        name="sent",
    ),
    path(
        "sent/<int:pk>/",
        view=views.OrderSentDetailView.as_view(),
        name="sent-detail",
    ),


]

"""

path(
    "sent/",
    view=views.OrderSentTemplateView.as_view(),
    name="sent",
),
"""
