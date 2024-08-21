# hotel/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# from django.contrib.auth.forms import UserCreationForm

from .models import Room, Booking, InventoryItem, RoomType,Contactus,Visitor
from .forms import BookingForm, InventoryItemForm, RoomTypeForm, RoomForm, UpdateRoomForm,UpdateRoomCategoryForm,ContactUsForm

def homepage(request):
    return render(request, 'hotel/homepage.html')


def home(request):
    rooms = Room.objects.all()[0:3]
    return render(request, 'hotel/home.html', {'rooms': rooms})

# @login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room
            booking.save()
            room.is_available = False
            room.save()
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'hotel/book_room.html', {'form': form, 'room': room})

# def registration(request):
#     form = UserCreationForm()
#     context = {'form':form}
#     return render(request, 'hotel/register.html',context)

def view_booking(request):
    booking = Booking.objects.all()
    context = {'booking':booking}
    return render(request, 'hotel/view_booking.html', context)

def delete_view_booking(request, pk):
    booking = Booking.objects.get(pk=pk)
    booking.delete()
    return redirect('view-booking')

# def update_view_booking(request, pk):
#     booking = Booking.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = UpdateVieBookingForm(request.POST, instance=booking)
#         if form.is_valid():
#             form.save()
#             return redirect('view-booking')
#     else:
#         form = UpdateVieBookingForm(instance=booking)
#     context = {'booking':booking,'form':form}
#     return render(request, 'hotel/view_booking.html',context)

def explore(request):
    return render(request, 'hotel/explore.html')


# @login_required
def inventory(request):
    items = InventoryItem.objects.all()
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view-inventory-page')
    else:
        form = InventoryItemForm()
    return render(request, 'hotel/inventory.html', {'items': items, 'form': form})

def view_inventory_page(request):
    items = InventoryItem.objects.all()
    context = {'items':items}
    return render(request, 'hotel/view_inventory_page.html',context)

# @login_required
def manage_rooms(request):
    rooms = Room.objects.all()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_rooms')
    else:
        form = RoomForm()
    return render(request, 'hotel/add_rooms.html', {'rooms': rooms, 'form': form})

# @login_required
def manage_room_types(request):
    room_types = RoomType.objects.all()
    if request.method == 'POST':
        form = RoomTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_types')
    else:
        form = RoomTypeForm()
    return render(request, 'hotel/room_types.html', {'room_types': room_types, 'form': form})


def update_room_category(request, pk):
    roomtype = RoomType.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateRoomCategoryForm(request.POST, instance=roomtype)
        if form.is_valid():
            form.save()
            return redirect('room_types')
    else:
        form = UpdateRoomCategoryForm(instance=roomtype)
    context ={'roomtype':roomtype,'form':form}
    return render(request, 'hotel/room_types.html',context)


def delete_category(request, pk):
    roomtype = RoomType.objects.get(pk=pk)
    roomtype.delete()
    return redirect('room_types')
            


def update_room(request, pk):
    room = Room.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateRoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('add_rooms')
    else:
        form = UpdateRoomForm(instance=room)
    context = {'room':room,'form':form}
    return render(request, 'hotel/add_rooms.html',context)


def delete_room(request, pk):
    room = Room.objects.get(pk=pk)
    room.delete()

    return redirect('add_rooms')
    
def contactus(request):
    contacts = Contactus.objects.all()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return('contactus')
    else:
        form = ContactUsForm()
    context ={'form':form,'contacts':contacts}
            
    return render(request, 'hotel/contactus.html', context)


# def get_ip(request):
#     address = request.META.get('HTTP_X_FORWARDED_FOR')
#     if address:
#         ip = address.split(',')[-1].strip()
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#         return ip
    
#     ip=get_ip(request)
#     u=Visitor(visitor = ip)
#     result = Visitor.objects.filter(Q(visitor__icontains=ip))
#     if len(result)==1:
#         print('visitor exist')
#     elif len(result)>1:
#         print('visitor exist too ....')
#     else:
#         u.save()
#         print ('visitor is unique')
#     count = Visitor.objects.all().count()
#     print(count,'is your number of user')
#     context = {'count':count}
#     return render(request,'hotel/view_booking.html',context)
        
    
def get_ip(request):
    address = request.META.get('HTTP_X_FORWARDED_FOR')
    if address:
        ip = address.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def handle_visitor(request):
    ip = get_ip(request)
    u = Visitor(visitor=ip)
    
    # Check if the visitor already exists in the database
    result = Visitor.objects.filter(Q(visitor__icontains=ip))
    
    if result.exists():
        if result.count() == 1:
            print('Visitor exists')
        else:
            print('Visitor exists too many times....')
    else:
        u.save()
        print('Visitor is unique')
    
    # Count the number of visitors
    count = Visitor.objects.all().count()
    print(count, 'is your number of users')
    
    # Render the template with the context
    context = {'count': count}
    return render(request, 'hotel/view_booking.html', context)