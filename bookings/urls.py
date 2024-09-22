from django.urls import path
from . import views

urlpatterns = [
    path('book-appointment/<int:service_id>/', views.book_appointment, name='book_appointment'),
]
