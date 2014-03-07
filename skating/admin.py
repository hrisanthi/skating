from django.contrib import admin
from skating.models import Athlete

class AthleteAdmin(admin.ModelAdmin):
    search_fields = ('name',)
admin.site.register(Athlete, AthleteAdmin)



