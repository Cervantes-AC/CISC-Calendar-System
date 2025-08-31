# backend/apps/calendar/models.py
from django.db import models
from django.conf import settings
from datetime import datetime

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)  # Admin approves or rejects

    STATUS_CHOICES = [
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.title} on {self.date} at {self.time}"

    @property
    def start_datetime(self):
        """Combine date and time into a single datetime object for easy use."""
        return datetime.combine(self.date, self.time)
