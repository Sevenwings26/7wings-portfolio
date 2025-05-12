from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
from .forms import UserRegistrationForm

# Generate auth token 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site

# set auth timeout 
# from django.core.signing import TimestampSigner, SignatureExpired, BadSignature


# customized model
User = get_user_model()

def register_view(request):
    """
    User registration
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.is_active = False  # User not active - 0 
            user.save()
            # email = form.cleaned_data['email']

            # Generate email verification token
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            domain = get_current_site(request).domain
            verification_link = f"http://{domain}/activate/{uid}/{token}/"

            # Send email
            subject = "Verify Your Email"
            html_message = render_to_string('emails/verify-account.html', {
                'user': user,
                'verification_link': verification_link
            })

            email = EmailMessage(
                subject=subject,
                from_email=settings.EMAIL_HOST_USER,
                to=[user.email],
                body=html_message
            )
            
            email.content_subtype = "html"
            email.send()     
            messages.success(request, "A verification email has been sent. Please check your inbox.")
            return redirect('login')        
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/registration/register.html', {'form': form})


def activate_account(request, uidb64, token):
    """
    Function activates account when URL in email is clicked
    """
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your account has been successfully activated! You can now log in.")
        return redirect('login')  
    else:
        messages.error(request, "Invalid or expired activation link.")
        return redirect('register')


    
# signer = TimestampSigner()

# def register_view(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.is_active = False  # Don't activate until email verified
#             user.save()

#             token = signer.sign(user.email)
#             verification_url = request.build_absolute_uri(
#                 reverse('verify_email', args=[token])
#             )

#             send_mail(
#                 subject='Verify Your Email',
#                 message=f'Click the link to verify your account (expires in 2 hours): {verification_url}',
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 recipient_list=[user.email],
#                 fail_silently=False,
#             )

#             messages.success(request, "Registration successful! Please check your email to verify.")
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'blog/registration/register.html', {'form': form})






# from django.utils.timezone import now, timedelta

# def verify_email_view(request, token):
#     try:
#         email = signer.unsign(token, max_age=7200)  # 2 hours = 7200s
#         user = CustomUser.objects.get(email=email)
#         user.is_active = True
#         user.save()
#         messages.success(request, "Email verified! You can now log in.")
#         return redirect('login')
#     except SignatureExpired:
#         messages.error(request, "Verification link has expired.")
#     except (BadSignature, CustomUser.DoesNotExist):
#         messages.error(request, "Invalid or tampered link.")
#     return redirect('register')
