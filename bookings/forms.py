from django import forms
from .models import Appointment
from datetime import datetime

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'min': datetime.now().strftime('%Y-%m-%d')}),
            'time': forms.TimeInput(attrs={'type': 'time', 'min': '08:00', 'max': '17:00'}),
            'notes': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Any special requests or notes...'}),
        }

    def clean_date(self):
        """ Ensure that previous dates cannot be booked """
        appointment_date = self.cleaned_data.get('date')
        if appointment_date < datetime.today().date():
            raise forms.ValidationError("You cannot book an appointment in the past.")
        return appointment_date
