from django.urls import path
from . import views

app_name = 'myresto'

urlpatterns = [
    path('resto/', views.resto_list, name='resto_list'),
    path('resto/<int:pk>/', views.resto_detail, name='resto_detail'),  # Gunakan pk, bukan id
]
