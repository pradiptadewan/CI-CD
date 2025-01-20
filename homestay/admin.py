from django.contrib import admin
from .models import Room, Booking


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_type', 'price', 'is_available', 'image_preview')  # Tambahkan field preview
    list_filter = ('room_type', 'is_available')
    search_fields = ('name', 'description')

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="width: 50px; height: auto;">'
        return "No Image"

    image_preview.allow_tags = True
    image_preview.short_description = 'Preview'

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'room', 'check_in_date', 'check_out_date', 'guests')
    list_filter = ('check_in_date', 'check_out_date', 'room')
    search_fields = ('customer_name', 'email')
