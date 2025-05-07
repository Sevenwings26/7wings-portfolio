from django.urls import path
from . import views

urlpatterns = [
    path("sign-up/", views.register_view, name="register"),       
    # path("verify/<str:token:>/", views.verify_email_view, name="verify_email"),       
]

