from django.contrib.admin import *
from .models import Hotel

@register(Hotel)
class HotelAdmin(ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')