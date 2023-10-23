from django.db.models import *
from apps.hotels.models import Hotel

class Room(Model):
    hotel = ForeignKey(Hotel, on_delete=CASCADE)
    number = IntegerField('Номер комнаты')
    capacity = PositiveIntegerField('Вместимость')
    price_per_night = PositiveIntegerField('Цена за одну ночь')

    def __str__(self):
        return f'{self.hotel.name} {self.number}'

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

