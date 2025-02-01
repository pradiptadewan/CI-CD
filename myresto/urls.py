from django.urls import path
from . import views
from .views import RestaurantListView

app_name = 'myresto'

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant_list'),
    path('resto/<int:pk>/', views.resto_detail, name='resto_detail'),
]
