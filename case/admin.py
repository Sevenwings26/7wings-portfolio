from django.contrib import admin
from .models import Service, ServiceFeature, Testimonial, Project

admin.site.register(Service)
admin.site.register(Project)
admin.site.register(ServiceFeature)
admin.site.register(Testimonial)

