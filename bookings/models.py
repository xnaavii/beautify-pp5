from django.db import models
from django.contrib.auth.models import User
from services.models import Service

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.service.name} on {self.appointment_date.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['appointment_date']