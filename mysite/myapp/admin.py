from django.contrib import admin

# Register your models here.
from .models import RaceTime



from django.contrib import admin



class RaceTimeAdmin(admin.ModelAdmin):
    search_fields = ('place', 'firstName', 'lastName', 'team', 'time', 'session', 'event', 'meet', 'date', 'score', 'bib', 'location', 'host', 'gender', 'sessionOrder')

admin.site.register(RaceTime, RaceTimeAdmin)
