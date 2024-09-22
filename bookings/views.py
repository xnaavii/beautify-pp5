from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from services.models import Service
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required

@login_required
def book_appointment(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST, service=service)  # Pass the service to the form
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user  # Assign the authenticated user
            appointment.service = service
            appointment.save()
            messages.success(request, "Your appointment has been booked successfully!")
            return redirect('home')  # Redirect to an appropriate page after booking
    else:
        form = AppointmentForm(service=service)  # Pass the service for pre-filling

    template = 'bookings/book_appointment.html'
    context = {'form': form, 'service': service}

    return render(request, template, context)
