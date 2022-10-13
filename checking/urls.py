
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.check_card, name = 'check_card'),
    path('publish/<str:card_id>', views.publish, name = 'publish'),
    path('delete_card/<str:card_id>', views.delete_card, name = 'delete_card')
]
