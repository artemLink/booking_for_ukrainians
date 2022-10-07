from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about),
    path('register/', views.register),
    path('logout/', views.user_logout, name = 'logout'),
    path('user_login/', views.user_login, name='user_login'),
    path('view_card/<int:card_id>', views.view_card, name = 'show_card'),

]

