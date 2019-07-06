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
        "<int:pk>/<int:employee_pk>/",
        view=views.KindOfClotheDetailView.as_view(),
        name="kind",
    ),

]
