from django.urls import path
from .import views

urlpatterns = [
    path('acc/', views.index, name="index"),
]


