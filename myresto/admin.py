from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    # Menampilkan kolom nama, kategori, dan harga pada daftar menu
    list_display = ('name', 'category', 'price')

    # Menambahkan filter berdasarkan kategori
    list_filter = ('category',)

    # Menambahkan fitur pencarian berdasarkan nama dan deskripsi
    search_fields = ('name', 'description')

    # Menambahkan fitur untuk mengedit kategori menu secara cepat
    list_editable = ('category',)
