from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import HotelSerializer, RoomSerializer, GuestSerializer, BookingSerializer
from apps.hotels.models import Hotel
from apps.room.models import Room
from apps.guest.models import Guest
from apps.booking.models import Booking

class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes= [IsAdminUser]
    authentication_classes= [JWTAuthentication]

class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes= [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class GuestViewSet(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]