from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from .models import Room, Booking, MenuItem
from .forms import ContactForm, ReservationForm

class IndexView(TemplateView):
    template_name = 'homestay/index.html'

class RoomListView(ListView):
    model = Room
    template_name = 'homestay/room_list.html'
    context_object_name = 'rooms'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        room_type = self.request.GET.get('type')

        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )

        if room_type:
            queryset = queryset.filter(room_type=room_type)

        # Menambahkan urutan yang jelas untuk pagination
        return queryset.order_by('name')  # Atau berdasarkan field lain yang diinginkan

class RoomDetailView(DetailView):
    model = Room
    template_name = 'homestay/room_detail.html'  # Template untuk halaman detail
    context_object_name = 'room'  # Nama variabel untuk data di template


class ContactView(FormView):
    template_name = 'homestay/contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.save()  # Simpan data kontak ke database atau kirim email
        messages.success(self.request, "Pesan Anda telah terkirim!")
        return redirect('contact')

class ReservationView(FormView):
    template_name = 'homestay/reservation.html'
    form_class = ReservationForm

    def form_valid(self, form):
        form.save()  # Simpan data reservasi ke database
        messages.success(self.request, "Reservasi Anda berhasil dibuat!")
        return redirect('reservation')

class RestaurantListView(ListView):
    model = MenuItem
    template_name = 'resto/resto_list.html'
    context_object_name = 'items'
    paginate_by = 6  # Adjust as needed

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )

        return queryset.order_by('name')  # Or use another ordering field if needed
