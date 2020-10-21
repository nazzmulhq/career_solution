"""Carisor URL Configuration

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
    2. Add a URL to urlpatterns:  path('blogsite/', include('blogsite.urls'))
"""

from django.urls import path
from WebSite import views

app_name = 'WebSite'

urlpatterns = [

    path('', views.index, name='home'),
    path('carisor/about', views.about, name='about'),
    path('carisor/career', views.career, name='career'),
    path('carisor/institution/', views.institution, name='institution'),
    path('carisor/institution_filter/<int:types>/', views.filters, name='filter'),
    path('carisor/courses/', views.courses, name='courses'),
    path('carisor/courses/<int:id>/', views.courses_details_filters, name='courses_filter'),
    path('carisor/directory/', views.directory, name='directory'),
    path('carisor/tools/junior/', views.junior_predict, name='junior_predict'),
    path('carisor/tools/science/', views.science, name='science'),
    path('carisor/tools/arts/', views.arts, name='arts'),
    path('carisor/tools/commerce/', views.commerce, name='commerce'),
    path('carisor/tools/careerguides/', views.careerguides, name='careerguides'),
    path('carisor/tools/computer/', views.computer, name='computer'),


]
