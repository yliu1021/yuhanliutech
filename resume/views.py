import os
import mimetypes

from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Experience, Education, Skill, Award


def index(request):
    experiences = Experience.objects.order_by('-start_date')
    educations = Education.objects.order_by('-start_date')
    skills = Skill.objects.order_by('-expertise')
    awards = Award.objects.order_by('-received_date')
    return render(request, 'resume.html', {
        'experiences': experiences,
        'educations': educations,
        'skills': skills,
        'awards': awards,
    })


def download(request):
    filename = 'Yuhan_LIU_UCLA.pdf'
    file_path = os.path.join('resume/downloads', filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            mime_type, _ = mimetypes.guess_type(file_path)
            response = HttpResponse(file.read(), content_type=mime_type)
            response['Content-Disposition'] = f'inline; filename={filename}'
            return response
    else:
        return Http404
