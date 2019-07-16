from django.urls import path

from . import views

app_name = "employees"
urlpatterns = [
    path(
        "",
        view=views.EmployeesListView.as_view(),
        name="employees",
    ),
    path(
        "<int:pk>",
        view=views.EmployeeDetailView.as_view(),
        name="employee",
    ),

]
