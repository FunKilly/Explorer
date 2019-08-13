from django.contrib import admin
from .models import Event, Place

class PlanPlaceInline(admin.TabularInline):
    model = Place
    raw_id_fields = ['place']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created', 'updated']
    list_filter = ['created', 'updated']
    inlines = [PlanPlaceInline]