from django.urls import path

from . import views

app_name = "ubrania"
urlpatterns = [
    path(
        "",
        view=views.RodzajUbraniaListView.as_view(),
        name="rodzaje",
    ),

]
