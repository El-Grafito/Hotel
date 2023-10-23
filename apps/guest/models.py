from django.db.models import *

class Guest(Model):
    first_name = CharField('Фамилия', max_length=255)
    last_name = CharField('Имя', max_length=255)
    email = CharField('Эл. Почта', max_length=255, blank=True, null=True)
    phone_number = CharField('Телефонный номер', max_length=15, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'