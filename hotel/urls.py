# hotel/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home/', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    # path('register/', views.registration, name='register'),
    
    path('book_room/<int:room_id>/', views.book_room, name='book_room'),
    path('view-booking/', views.view_booking, name='view-booking'),
    path('delete-view-booking/<int:pk>', views.delete_view_booking, name='delete-view-booking'),
    
    path('inventory/', views.inventory, name='inventory'),
    path('view-inventory-page/', views.view_inventory_page, name='view-inventory-page'),
    path('add_rooms/', views.manage_rooms, name='add_rooms'),
    path('room_types/', views.manage_room_types, name='room_types'),
    path('contactus/', views.contactus, name='contactus'),
    
    
    path('update_room/<int:pk>', views.update_room, name='update_room'),
    path('delete-room/<int:pk>', views.delete_room, name='delete-room'),
    
    
    path('update-room-category/<int:pk>', views.update_room_category, name='update-room-category'),
    path('delete-category/<int:pk>', views.delete_category, name='delete-category'),
    
    path('track-visitor/', views.handle_visitor, name='track_visitor'),
]
