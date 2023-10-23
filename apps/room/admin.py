from django.contrib.admin import *
from .models import Room

class RoomAdmin(ModelAdmin):
    list_display = ('id', 'number')
    list_display_links = ('id', 'number')