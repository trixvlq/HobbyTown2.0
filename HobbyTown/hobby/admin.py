from django.contrib import admin
from .models import *


class EventGameInline(admin.TabularInline):
    model = EventGame


class EventAdmin(admin.ModelAdmin):
    inlines = [EventGameInline]


admin.site.register(Game)
admin.site.register(Event,EventAdmin)
admin.site.register(EventGame)
admin.site.register(SpecialSign)
admin.site.register(RegularSign)
