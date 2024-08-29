from django.shortcuts import render, redirect
from .models import GeneralInfo, Service
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    services = Service.objects.all()

    general_records = GeneralInfo.objects.first()
    context = {
        "brand_name": general_records.brand_name,
        "username": general_records.name,
        "phone": general_records.phone,
        "description": general_records.description,
        "title1":general_records.title_one,
        "title2":general_records.title_two,
        "title3":general_records.title_three,
        "title4":general_records.title_four,
        "x_url":general_records.x_url,
        "f_url":general_records.f_url,
        "ig_url":general_records.ig_url,
        "linkedin_url":general_records.linkedin_url,

        "services":services,
    }
    return render(request, "pages/index.html", context)


# contact form  
def contact_form(request):
    if request.method == "POST":
        print("User submitted form...")
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # send mail .... 
        send_mail(
            subject=subject,
            message=f"{name} - {email} - {message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False, # True is default
        )
        

    return redirect('index')