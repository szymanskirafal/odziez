from django.urls import path

from . import views

app_name = "orders"
urlpatterns = [
    path(
        "redirect/<int:kind_pk>/<int:employee_pk>/",
        view=views.OrderTemplateView.as_view(),
        name="redirect",
    ),

]
