from django.urls import path
from . import views

urlpatterns = [
    path('', views.upcoming_appointments, name='upcoming_appointments'),
    path('book-appointment/<int:service_id>/', views.book_appointment, name='book_appointment'),
    path('booking_success/<int:appointment_id>/', views.booking_success, name='booking_success'),
]
