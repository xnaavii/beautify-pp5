from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    service_name = forms.CharField(required=False, disabled=True)
    service_price = forms.DecimalField(required=False, disabled=True)

    class Meta:
        model = Appointment
        fields = ['appointment_date', 'notes', 'service_name', 'service_price']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        service = kwargs.pop('service', None)
        super().__init__(*args, **kwargs)
        if service:
            self.fields['service_name'].initial = service.name
            self.fields['service_price'].initial = service.price
            self.fields['notes'].widget.attrs.update({'placeholder': 'Any special requests or notes...'})
