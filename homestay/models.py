from django.db import models
from django.core.validators import MinValueValidator

class Room(models.Model):
    ROOM_TYPES = [
        ('standard', 'Standard'),
        ('family', 'Family'),
    ]

    name = models.CharField(max_length=100, verbose_name='Room Name')  # Nama kamar
    description = models.TextField(verbose_name='Room Description')  # Deskripsi kamar
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES, verbose_name='Room Type')  # Jenis kamar
    capacity = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name='Capacity')  # Kapasitas kamar
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price per Night')  # Harga per malam
    is_available = models.BooleanField(default=True, verbose_name='Available')  # Status ketersediaan
    facilities = models.ManyToManyField('Facility', blank=True, related_name='rooms', verbose_name='Facilities')  # Fasilitas kamar

    def __str__(self):
        return f"{self.name} ({self.get_room_type_display()})"

    def formatted_price(self):
        return f"Rp{self.price:,.0f}"  # Format harga tanpa desimal


class RoomImage(models.Model):
    room = models.ForeignKey(Room, related_name='room_images', on_delete=models.CASCADE, verbose_name='Room')  # Hubungkan dengan room
    image = models.ImageField(upload_to='room_images/', verbose_name='Room Image')  # Gambar kamar
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name='Image Description')  # Deskripsi gambar

    def __str__(self):
        return f"Image of {self.room.name}"


class Facility(models.Model):
    name = models.CharField(max_length=100, verbose_name='Facility Name')  # Nama fasilitas
    icon = models.CharField(max_length=50, blank=True, null=True, verbose_name='Icon Class')

    def __str__(self):
        return self.name

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')  # Relasi ke kamar
    customer_name = models.CharField(max_length=100, verbose_name='Customer Name')  # Nama pelanggan
    email = models.EmailField(verbose_name='Email Address')  # Email pelanggan
    check_in_date = models.DateField(verbose_name='Check-in Date')  # Tanggal check-in
    check_out_date = models.DateField(verbose_name='Check-out Date')  # Tanggal check-out
    guests = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name='Number of Guests')  # Jumlah tamu

    def __str__(self):
        return f"{self.customer_name} - {self.room.name}"


class Wisata(models.Model):
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    harga_tiket_domestik = models.DecimalField(max_digits=10, decimal_places=2)
    harga_tiket_mancanegara = models.DecimalField(max_digits=10, decimal_places=2)
    jam_buka = models.CharField(max_length=100)

    def __str__(self):
        return self.judul

class FotoWisata(models.Model):
    wisata = models.ForeignKey(Wisata, related_name='galeri_foto', on_delete=models.CASCADE)
    gambar = models.ImageField(upload_to='galeri/')
    deskripsi = models.CharField(max_length=255)

    def __str__(self):
        return f"Foto dari {self.wisata.judul}"
