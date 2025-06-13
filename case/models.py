from django.db import models
from ckeditor.fields import RichTextField

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()

class ServiceFeature(models.Model):
    service = models.ForeignKey(Service, related_name='features', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
