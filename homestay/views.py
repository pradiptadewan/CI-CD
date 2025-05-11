from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.db.models import Q
from django.contrib import messages
from .models import Room, Wisata, FotoWisata
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
    template_name = 'homestay/room_detail.html'
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['facilities'] = self.object.facilities.all()  # Ambil fasilitas kamar
        context['other_rooms'] = Room.objects.exclude(pk=self.object.pk)[:5]  # Kamar lain

        # Mengambil gambar-gambar yang di-upload untuk kamar ini
        context['images'] = self.object.room_images.all()  # Menggunakan related_name yang benar

        return context



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

    def get_initial(self):
        initial = super().get_initial()
        room_id = self.request.GET.get('room_id')
        if room_id:
            try:
                room = Room.objects.get(pk=room_id)
                initial['room'] = room
            except Room.DoesNotExist:
                pass
        return initial

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Reservasi Anda berhasil dibuat!")
        return redirect('homestay:reservation')

def wisata_list(request):
    wisata = Wisata.objects.first()  # Ambil satu data wisata
    galeri_foto = FotoWisata.objects.filter(wisata=wisata)  # Ambil foto-foto wisata
    return render(request, 'homestay/wisata_list.html', {
        'wisata': wisata,
        'galeri_foto': galeri_foto
    })
