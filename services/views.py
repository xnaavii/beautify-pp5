from django.shortcuts import render, get_object_or_404
from .models import Service, Category

# Create your views here.
def service_list(request):
    """ View to return all the services """
    categories = Category.objects.all()
    services = Service.objects.all()
    template = 'services/service_list.html'
    context = {'services': services, 'categories': categories}
    return render(request, template, context)

def service_detail(request, service_id):
    """ View to return a detailed view for a single service """
    service = get_object_or_404(Service, id=service_id)
    template = 'services/service_detail.html'
    context = {'service': service}
    return render(request, template, context)