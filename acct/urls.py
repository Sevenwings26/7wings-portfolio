from django.urls import path
from . import views

urlpatterns = [
    path("sign-up/", views.register_view, name="register"),       
    path("activate/<uidb64>/<token>/", views.activate_account, name="activate"),
]

