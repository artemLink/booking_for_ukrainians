from django.urls import path
from . import views

urlpatterns = [
    path('single/<int:card_id>', views.rent_single_room, name = 'rent_single_room'),
    path('double/<int:card_id>', views.rent_single_room, name = 'rent_double_room'),
]