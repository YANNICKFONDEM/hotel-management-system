from django.contrib import admin
from .models import Booking,Room,RoomType,InventoryItem,Contactus,Visitor
# Register your models here.

admin.site.register(Booking)
admin.site.register(Room)
admin.site.register(InventoryItem)
admin.site.register(RoomType)
admin.site.register(Contactus)
admin.site.register(Visitor)