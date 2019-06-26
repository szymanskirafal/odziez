from django.urls import path

from . import views

app_name = "cart"
urlpatterns = [
    path(
        "add/",
        view=views.CartAddFormView.as_view(),
        name="add",
    ),

]
