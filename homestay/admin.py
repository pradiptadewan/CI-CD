from django.contrib import admin
from .models import Room, RoomImage, Booking, Facility
from django.utils.html import format_html

class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1  # Menampilkan satu form kosong untuk menambah gambar
    readonly_fields = ('image_preview',)  # Menampilkan preview gambar (opsional)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="width: 50px; height: auto;">'
        return "No Image"

    image_preview.allow_tags = True
    image_preview.short_description = 'Preview'

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_type', 'price', 'is_available')  # Menampilkan detail kamar
    list_filter = ('room_type', 'is_available')
    search_fields = ('name', 'description')
    filter_horizontal = ('facilities',)
    inlines = [RoomImageInline]  # Menambahkan inline untuk RoomImage

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

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_display')

    def icon_display(self, obj):
        if obj.icon:
            return format_html('<i class="fa {}"></i> {}'.format(obj.icon, obj.name))
        return obj.name

    icon_display.allow_tags = True
    icon_display.short_description = 'Icon'
