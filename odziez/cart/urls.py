from django.urls import path

from . import views

app_name = "cart"
urlpatterns = [
    path(
        "",
        view=views.cart_detail,
        name="detail",
    ),
    path(
        "add/<int:pracownik_pk>/<int:rodzaj_pk>/",
        view=views.CartAddFormView.as_view(),
        name="add",
    ),

]
