
from django import forms
from .models import Booking, InventoryItem, RoomType, Room,Contactus

# Form for booking a room
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['guest_phone','guest_email','check_in', 'check_out',]
        
        
class UpdateVieBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['guest_phone','guest_email','check_in', 'check_out',]

# Form for adding an inventory item
class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'quantity', 'description']
        
        

# Form for adding room types
class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = ['type_name', 'description']

# Form for adding rooms
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'price', 'is_available']


class UpdateRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields =  '__all__'
        
class UpdateRoomCategoryForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields  = '__all__'
        

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields  = '__all__'
        


