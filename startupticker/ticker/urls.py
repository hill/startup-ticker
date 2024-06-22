from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("item/<str:slug>", views.item, name="item"),
]
