from distutils.command.upload import upload
import email
from hashlib import blake2b
from importlib.metadata import requires
from django.db import models

# Create your models here.


class RoomsAvailable(models.Model):
    image=models.ImageField(upload_to="products/" , blank=False)
    title=models.TextField(max_length=1000,blank=False)
    amount=models.IntegerField(blank=False)
    available=models.IntegerField(blank=False)
    def __str__(self) -> str:
        return str(self.title)


class RoomsList(models.Model):
    fkey=models.ForeignKey(RoomsAvailable, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    list=models.TextField(blank=False)
    def __str__(self) -> str:
        return str(self.fkey)


class Bookings(models.Model):
    user=models.TextField(blank=False)
    email=models.TextField(blank=False)
    sex=models.TextField(blank=False)
    dob=models.TextField(blank=False)
    address=models.TextField(blank=False)
    cin=models.TextField(blank=False)
    number=models.TextField(blank=False)
    cout=models.TextField(blank=False)
    roomname=models.TextField(blank=False)
    amount=models.IntegerField(blank=False)
    mode=models.TextField(blank=False)
    def __str__(self) -> str:
        return str(self.user)