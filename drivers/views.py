from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from drivers.forms import DriverForm
from drivers.models import Driver


class DriverUpdateView(SuccessMessageMixin,
                       UpdateView):
    model = Driver
    form_class = DriverForm
    success_url = reverse_lazy("home")
    success_message = "Информация о водителе сохранена"


class DriverCreateView(SuccessMessageMixin,
                       CreateView):
    model = Driver
    form_class = DriverForm
    success_url = reverse_lazy("home")
    success_message = "Информация о водителе сохранена"
