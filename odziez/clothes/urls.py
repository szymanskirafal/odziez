from django.urls import path

from . import views

app_name = "clothes"
urlpatterns = [
    path(
        "",
        view=views.KindsOfClothesListView.as_view(),
        name="kinds",
    ),
    path(
        "<int:kind_pk><int:order_pk><int:employee_pk>/",
        view=views.ClotheCreateView.as_view(),
        name="clothe-create",
    ),

]
