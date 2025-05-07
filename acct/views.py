from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.signing import TimestampSigner, SignatureExpired, BadSignature
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .forms import UserRegistrationForm
from .models import CustomUser

# Create your views here.

signer = TimestampSigner()

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False  # Don't activate until email verified
            user.save()

            token = signer.sign(user.email)
            verification_url = request.build_absolute_uri(
                reverse('verify_email', args=[token])
            )

            send_mail(
                subject='Verify Your Email',
                message=f'Click the link to verify your account (expires in 2 hours): {verification_url}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )

            messages.success(request, "Registration successful! Please check your email to verify.")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/registration/register.html', {'form': form})


# from django.utils.timezone import now, timedelta

def verify_email_view(request, token):
    try:
        email = signer.unsign(token, max_age=7200)  # 2 hours = 7200s
        user = CustomUser.objects.get(email=email)
        user.is_active = True
        user.save()
        messages.success(request, "Email verified! You can now log in.")
        return redirect('login')
    except SignatureExpired:
        messages.error(request, "Verification link has expired.")
    except (BadSignature, CustomUser.DoesNotExist):
        messages.error(request, "Invalid or tampered link.")
    return redirect('register')
