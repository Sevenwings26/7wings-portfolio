from django.shortcuts import render
from datetime import datetime

# Create your views here.
"""
    CONTAINS PORTFOLIO LOGICS
""" 
from django.shortcuts import render, redirect, get_object_or_404

# use application model 
from application.models import GeneralInfo, Frontendskill, Backend_dataskill, ContactFormLog
from .models import Service, ServiceFeature, Testimonial, Project
# for mail 
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils import timezone


# current_year = datetime.today()
# current_year = datetime(current_year.year)

# Create your views here.
def index(request):
    services = Service.objects.all()[:4]
    testimonials = Testimonial.objects.all()
    projects = Project.objects.all()[:3]

    # Fetch the first general record or None if it doesn't exist
    general_records = GeneralInfo.objects.first()

    # Initialize context using getattr for all attributes, with default values
    context = {
        "brand_name": getattr(general_records, "brand_name", "Sevenwings"),
        "first_name": getattr(general_records, "first_name", "Iyanu"),
        "last_name": getattr(general_records, "last_name", "Arowosola"),
        "phone": getattr(general_records, "phone", "N/A"),
        "email": getattr(general_records, "email", "N/A"),
        "address": getattr(general_records, "address", "N/A"),
        "description": getattr(general_records, "description", "N/A"),
        "title1": getattr(general_records, "title_one", "N/A"),
        "title2": getattr(general_records, "title_two", "N/A"),
        "title3": getattr(general_records, "title_three", "N/A"),
        "title4": getattr(general_records, "title_four", "N/A"),
        "resume_link": getattr(general_records, "resume_link", "N/A"),

        "x_url": getattr(general_records, "x_url", "#"),
        "f_url": getattr(general_records, "f_url", "#"),
        "ig_url": getattr(general_records, "ig_url", "#"),
        "linkedin_url": getattr(general_records, "linkedin_url", "#"),
        "github_url": getattr(general_records, "github_url", "#"),
        "location": getattr(general_records, "location", "N/A"),
        "brief_bio": getattr(general_records, "brief_bio", "N/A"),
        "bio": getattr(general_records, "bio", "N/A"),

        # update models - 6th June, 2025.
        "about_title": getattr(general_records, "about_title", "About Me"),
        "hero_caption": getattr(general_records, 'hero_caption', "N/A"),
        "service_caption": getattr(general_records, 'service_caption', "N/A"),

    }

    # Add services to the context
    context["services"] = services
    context["testimonials"] = testimonials
    context["projects"] = projects

    return render(request, "case/landing.html", context)



def about(request):
    general_records = GeneralInfo.objects.first()

    # Initialize context using getattr for all attributes, with default values
    context = {
        "brand_name": getattr(general_records, "brand_name", "Sevenwings"),
        "first_name": getattr(general_records, "first_name", "Iyanu"),
        "last_name": getattr(general_records, "last_name", "Arowosola"),
        "phone": getattr(general_records, "phone", "N/A"),
        "email": getattr(general_records, "email", "N/A"),
        "address": getattr(general_records, "address", "N/A"),
        "x_url": getattr(general_records, "x_url", "#"),
        "f_url": getattr(general_records, "f_url", "#"),
        "ig_url": getattr(general_records, "ig_url", "#"),
        "linkedin_url": getattr(general_records, "linkedin_url", "#"),
        "github_url": getattr(general_records, "github_url", "#"),
        "location": getattr(general_records, "location", "N/A"),
        "bio": getattr(general_records, "bio", "N/A"),

        # update models - 6th June, 2025.
        "about_title": getattr(general_records, "about_title", "About Me"),
        "hero_caption": getattr(general_records, 'hero_caption', "N/A"),
        "service_caption": getattr(general_records, 'service_caption', "N/A"),
    }

    return render(request, 'case/about.html', context)



# Portfolio page
def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'case/projects.html', {})

def services(request):
    testimonial = Testimonial.objects.all()
    services = Service.objects.prefetch_related('features').all()
    context = {
        'services': services
    }
    context["testimonial"] = testimonial

    return render(request, 'case/services.html', context)

