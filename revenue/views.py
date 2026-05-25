from django.views.generic import ListView

from revenue.models import Revenue


class RevenueListView(ListView):
    model = Revenue

    def get_queryset(self):
        queryset = Revenue.objects.filter(driver__pk=self.kwargs.get("pk"))
        return queryset