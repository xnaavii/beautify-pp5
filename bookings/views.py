from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from services.models import Service
from .models import Appointment
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required

@login_required
def book_appointment(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.service = service
            appointment.save()
            messages.success(request, "Your appointment has been booked successfully!")
            return redirect('booking_success', appointment_id=appointment.id)
        else:
            print("Form errors:", form.errors)  # Output form errors
    else:
        form = AppointmentForm()

    context = {'form': form, 'service': service}
    return render(request, 'bookings/book_appointment.html', context)

@login_required
def booking_success(request, appointment_id):
    """A view to redirect user to the booking successful page"""
    
    appointment = get_object_or_404(Appointment, id=appointment_id)
    template = "bookings/booking_success.html"
    context = {"appointment": appointment}
    
    return render(request, template, context )


@login_required
def upcoming_appointments(request):
    """A view to display user's upcoming appointments and handle cancellations."""
    appointments = Appointment.objects.filter(user=request.user).order_by('appointment_date')

    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)
        appointment.delete()
        messages.success(request, "Your appointment has been cancelled successfully!")
        return redirect('upcoming_appointments')

    return render(request, 'bookings/upcoming_appointments.html', {'appointments': appointments})
