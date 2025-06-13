"""
    CONTAINS PORTFOLIO LOGICS
""" 

from django.shortcuts import render, redirect, get_object_or_404
from .models import GeneralInfo, Service, Frontendskill, Backend_dataskill, ContactFormLog

# for mail 
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils import timezone


# Create your views here.
def index(request):
    services = Service.objects.all()

    # Fetch the first general record or None if it doesn't exist
    general_records = GeneralInfo.objects.first()

    # Initialize context using getattr for all attributes, with default values
    context = {
        "brand_name": getattr(general_records, "brand_name", "Default Brand"),
        "username": getattr(general_records, "name", "Default Name"),
        "phone": getattr(general_records, "phone", "N/A"),
        "email": getattr(general_records, "email", "N/A"),
        "address": getattr(general_records, "address", "N/A"),
        "description": getattr(general_records, "description", "N/A"),
        "title1": getattr(general_records, "title_one", "N/A"),
        "title2": getattr(general_records, "title_two", "N/A"),
        "title3": getattr(general_records, "title_three", "N/A"),
        "title4": getattr(general_records, "title_four", "N/A"),
        "x_url": getattr(general_records, "x_url", "#"),
        "f_url": getattr(general_records, "f_url", "#"),
        "ig_url": getattr(general_records, "ig_url", "#"),
        "linkedin_url": getattr(general_records, "linkedin_url", "#"),
        "github_url": getattr(general_records, "github_url", "#"),
        "about_title": getattr(general_records, "about_title", "About Me"),
        "degree": getattr(general_records, "degree", "N/A"),
        "job_type": getattr(general_records, "job_type", "N/A"),
        "location": getattr(general_records, "location", "N/A"),
        "bio": getattr(general_records, "bio", "N/A"),
    }

    # Add services to the context
    context["services"] = services

    return render(request, "pages/index.html", context)


def service_detail(request, slug):
    titles = Service.objects.all() # get titles
    # service_detail = get_object_or_404(Service, id=service_id)
    # service_detail = get_object_or_404(Service, slug=slug)
    service_detail = Service.objects.get(slug=slug)
    context = {
        'service':service_detail,
        'titles':titles
    }
    return render(request, 'pages/service-details.html', context)


# contact form  
def contact_form(request):
    if request.method == "POST":
        print("Form Submitted...")
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Styling sent contact message
        context = {
            "name":name,
            "email":email,
            "subject":subject,
            "message":message,
        }

        html_context = render_to_string('email.html', context)
        
        is_success = False        
        is_error = False
        error_message = ""        

        # send mail .... 
        try:
            send_mail(
                subject=subject,
                # message=f"{name} - {email} - {message}",
                message=None,
                html_message=html_context,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False, # True is default
            )
        except Exception as e:
            is_error = True
            error_message = str(e)
            print(f'Email failed')
            messages.error(request, "There is an error, could not send email!")
        else:
            is_success = True
            print(f"Email has been sent out...")
            messages.success(request, "Email has been sent successfully!")

        # Contact form log 
        ContactFormLog.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            sent_time=timezone.now(),
            is_success=is_success,
            is_error=is_error,
            error_message=error_message,
        )

    return redirect('index')


# about page
def about(request):
    frontendskills = Frontendskill.objects.all()
    backendskills = Backend_dataskill.objects.all()

    # Fetch the first general record or None if it doesn't exist
    general_records = GeneralInfo.objects.first()

    # Initialize context using getattr for all attributes, with default values
    context = {
        "brand_name": general_records.brand_name,
        
        "brand_name": getattr(general_records, "brand_name", "Default Brand"),
        "phone": getattr(general_records, "phone", "N/A"),
        "email": getattr(general_records, "email", "N/A"),
        "description": getattr(general_records, "description", "N/A"),
        "about_title": getattr(general_records, "about_title", "About Me"),
        "degree": getattr(general_records, "degree", "N/A"),
        "job_type": getattr(general_records, "job_type", "N/A"),
        "location": getattr(general_records, "location", "N/A"),
        "bio": getattr(general_records, "bio", "N/A"),

        # Skills 
        "frontendskills": frontendskills,
        "backendskills": backendskills,
    }

    return render(request, "pages/about.html", context)


# Resume page  
def resume(request):
    general_records = GeneralInfo.objects.first()
    return render(request, 'pages/resume.html', {"resume":getattr(general_records, 'resume', "N/A")})

# Portfolio page
def portfolio(request):
    return render(request, 'pages/portfolio.html', {})

