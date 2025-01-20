from django.urls import path

from . import views
from .views import (
    IndexView, RoomListView, RoomDetailView,
    ContactView, ReservationView, RestaurantListView
)

app_name = 'homestay'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('rooms/', RoomListView.as_view(), name='room_list'),
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('reservation/', ReservationView.as_view(), name='reservation'),
    path('restaurants/', RestaurantListView.as_view(), name='restaurant_list'),
]
