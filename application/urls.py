from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact_form, name="contact"),
    path('about/', views.about, name="about"),
    path('resume/', views.resume, name="resume"),
    path('portfolio/', views.portfolio, name="portfolio"),
]