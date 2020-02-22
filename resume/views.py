from django.shortcuts import render
from .models import Experience, Education


def index(request):
    experiences = Experience.objects.order_by('-start_date')
    educations = Education.objects.order_by('-start_date')
    return render(request, 'resume.html', {'experiences': experiences,
                                           'educations': educations})
