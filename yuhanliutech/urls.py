"""yuhanliutech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blogs/', include('blogs.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

import homepage.views
import resume.views
import projects.views
import blogs.views


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('', RedirectView.as_view(url='home/', permanent=True)),
    path('home/', homepage.views.index, name='home'),
]

urlpatterns += [
    path('resume/', resume.views.index, name='resume'),
    path('resume/Yuhan_LIU_UCLA.pdf', resume.views.download, name='resume_download')
]

urlpatterns += [
    path('projects/', projects.views.index, name='projects'),
]

urlpatterns += [
    path('blogs/', blogs.views.index, name='blogs'),
]
