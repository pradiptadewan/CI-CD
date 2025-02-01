from django.urls import path

from . import views
from .views import (
    RoomListView, RoomDetailView,
    ContactView, ReservationView
)

app_name = 'homestay'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('rooms/', RoomListView.as_view(), name='room_list'),
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('reservation/', ReservationView.as_view(), name='reservation'),
    path('list/', views.wisata_list, name='wisata_list'),
]
