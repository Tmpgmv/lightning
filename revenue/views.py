from django.views.generic import ListView

from revenue.models import Revenue


class RevenueListView(ListView):
    model = Revenue