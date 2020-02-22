from django.shortcuts import render
from .models import Experience


def index(request):
    experiences = Experience.objects.order_by('-start_date')
    return render(request, 'resume.html', {'experiences': experiences})
