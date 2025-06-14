from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('serices/', views.services, name="services"),
    # path('contact/', views.contact, name="contact"),
    path('about-me/', views.about, name="about-me"),
]

