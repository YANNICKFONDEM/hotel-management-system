from django.db import models
from django.contrib.auth.models import User

class RoomType(models.Model):
    type_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.type_name

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    img = models.ImageField(upload_to='images', null=True, blank=True)
    def __str__(self):
        return f'Room {self.room_number} - {self.room_type.type_name}'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guest_email = models.EmailField(max_length=254)
    guest_phone = models.CharField(max_length=20)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f'Booking by {self.user.username} for room {self.room.room_number}'

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Contactus(models.Model):
    name = models.CharField(max_length=50,)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
class Visitor(models.Model):
    vissitor=models.TextField(default=None) 
    def __str__(self):
        return self.vissitor
    
    
