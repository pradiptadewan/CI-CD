from django.shortcuts import render, get_object_or_404
from .models import MenuItem, Resto
from django.views.generic import ListView
from django.db.models import Q


class RestaurantListView(ListView):
    model = MenuItem
    template_name = 'resto/resto_list.html'
    context_object_name = 'items'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )

        return queryset.order_by('name')


def resto_detail(request, pk):
    resto = get_object_or_404(Resto, pk=pk)

    # Mengambil resto lain selain yang sedang dilihat
    other_restos = Resto.objects.exclude(pk=pk)[:5]  # Misalnya, 5 resto lainnya

    return render(request, 'resto/resto_detail.html', {
        'resto': resto,
        'other_restos': other_restos
    })
