#from attr import fields
from django.contrib import admin
from .models import Venue
from .models import ClubUser 
from .models import Event

# Register your models here.

# admin.site.register(Venue)
admin.site.register(ClubUser)
#admin.site.register(Event)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address','phone')
    ordering = ('name',)
    search_fields  = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    feilds = (('name', 'venue'),'event_date','description','manager')  
    list_display = ('name','event_date','venue')  
    list_filter  = ('event_date','venue')
    ordering = ('-event_date',)