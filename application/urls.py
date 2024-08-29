from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact_form, name="contact")
]