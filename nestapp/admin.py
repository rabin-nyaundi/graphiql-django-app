from django.contrib import admin
from .models import Trip, Location, TripLocation


admin.site.register(Trip)
admin.site.register(Location)
admin.site.register(TripLocation)