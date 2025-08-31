# backend/apps/calendar/admin.py
from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'created_by', 'status')
    list_filter = ('status', 'date')
    search_fields = ('title', 'description', 'created_by__username')
