from rest_framework.serializers import *

from apps.hotels.models import Hotel
from apps.room.models import Room
from apps.guest.models import Guest
from apps.booking.models import Booking

class HotelSerializer(Serializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class RoomSerializer(Serializer):
    class Meta:
        model = Room
        fields = '__all__'

class GuestSerializer(Serializer):
    class Meta:
        model = Guest
        fields = '__all__'

class BookingSerializer(Serializer):
    class Meta:
        model = Booking
        fields = '__all__'