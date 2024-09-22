from django.shortcuts import render
from .models import Service, Category

# Create your views here.
def service_list(request):
    """ View to return all the services """
    categories = Category.objects.all()
    services = Service.objects.all()
    template = 'services/service_list.html'
    context = {'services': services, 'categories': categories}
    return render(request, template, context)