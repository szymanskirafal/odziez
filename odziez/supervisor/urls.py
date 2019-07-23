from django.urls import path

from . import views

app_name = "supervisor"
urlpatterns = [
    path(
        "",
        view=views.SupervisorDashboardTemplateView.as_view(),
        name="dashboard",
    ),
    path(
        "order/<int:pk>",
        view=views.SupervisorOrderDetailView.as_view(),
        name="order",
    ),

]
