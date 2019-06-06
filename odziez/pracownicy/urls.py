from django.urls import path

from . import views

app_name = "pracownicy"
urlpatterns = [
    path(
        "",
        view=views.PracownicyListView.as_view(),
        name="pracownicy",
    ),
    path(
        "<int:pk>",
        view=views.PracownikDetailView.as_view(),
        name="pracownik",
    ),

]
