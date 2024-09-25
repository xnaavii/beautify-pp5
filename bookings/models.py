from django.db import models
from django.contrib.auth.models import User
from services.models import Service

class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.service.name} at {self.time} on {self.date}"

    class Meta:
        ordering = ['date']