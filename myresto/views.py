from django.shortcuts import render, get_object_or_404
from .models import MenuItem, Resto


def resto_list(request):
    items = MenuItem.objects.all()
    return render(request, 'resto/resto_list.html', {'items': items})


def resto_detail(request, pk):
    resto = get_object_or_404(Resto, pk=pk)

    # Mengambil resto lain selain yang sedang dilihat
    other_restos = Resto.objects.exclude(pk=pk)[:5]  # Misalnya, 5 resto lainnya

    return render(request, 'resto/resto_detail.html', {
        'resto': resto,
        'other_restos': other_restos
    })