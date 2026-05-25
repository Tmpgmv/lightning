from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from drivers.models import Driver


class DriverCreateView(SuccessMessageMixin,
                       CreateView):
    model = Driver
    fields = "__all__"
    success_url = reverse_lazy("home")
    success_message = "Информация о водителе добавлена"
