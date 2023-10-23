from django.db.models import *

class Hotel(Model):
    name = CharField('Название', max_length=255)
    adress = CharField('Адресс', max_length=255*3)
    city = CharField('Город', max_length=255)
    country = CharField('Страна', max_length=255)
    rating = DecimalField('Рейтинг', max_digits=10, decimal_places=5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'