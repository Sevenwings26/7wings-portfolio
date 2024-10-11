from django.shortcuts import render, redirect
from .models import GeneralInfo, Service, Frontendskill, Backend_dataskill, ContactFormLog
from ckeditor.fields import RichTextField

# for mail 
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils import timezone

# Create your views here.
def index(request):
    services = Service.objects.all()

    general_records = GeneralInfo.objects.first()
    context = {
        # "brand_name": general_records.brand_name,
        "brand_name": getattr(general_records, "brand_name"),
        "username": getattr(general_records, "name"),
        "phone": general_records.phone,
        "email": general_records.email,
        "address": general_records.address,
        "description": general_records.description,
        "title1":general_records.title_one,
        "title2":general_records.title_two,
        "title3":general_records.title_three,
        "title4":general_records.title_four,
        "x_url":general_records.x_url,
        "f_url":general_records.f_url,
        "ig_url":general_records.ig_url,
        "linkedin_url":general_records.linkedin_url,
        "github_url":general_records.github_url,
        
        "about_title":general_records.about_title,
        "degree":general_records.degree,
        "job_type":general_records.job_type,
        "location":general_records.location,
        "bio":general_records.bio,



        "services":services,
    }
    return render(request, "pages/index.html", context)


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

    general_records = GeneralInfo.objects.first()
    context = {
        "brand_name": general_records.brand_name,
        "phone": general_records.phone,
        "email": general_records.email,
        "description": general_records.description,
        
        "about_title":general_records.about_title,
        "degree":general_records.degree,
        "job_type":general_records.job_type,
        "location":general_records.location,
        "bio":general_records.bio,

        # skills 
        "frontendskills":frontendskills,
        "backendskills":backendskills,
    }
    return render(request, "pages/about.html", context)

# Resume page  
def resume(request):
    return render(request, 'pages/resume.html', {} )

# Portfolio page
def portfolio(request):
    return render(request, 'pages/portfolio.html', {})

