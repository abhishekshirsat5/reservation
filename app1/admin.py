from statistics import mode
from zoneinfo import available_timezones
from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(RoomsAvailable)
class RoomsAvailable(admin.ModelAdmin):
    list_display = ('image', 'title', 'amount', 'available')


@admin.register(RoomsList)
class RoomsList(admin.ModelAdmin):
    list_display = ('fkey', 'list')


# @admin.register(Bookings)
# class Bookings(admin.ModelAdmin):
#     list_display = ('user', 'email', 'sex', 'dob', 'address', 'cin', 'number', 'cout', 'roomname')


@admin.register(Bookingss)
class Bookings(admin.ModelAdmin):
    list_display = ('user', 'email', 'sex', 'dob', 'address', 'cin', 'number', 'cout', 'roomname','amount','mode')

