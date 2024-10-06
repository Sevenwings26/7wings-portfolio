from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class GeneralInfo(models.Model):
    brand_name = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    title_one = models.CharField(max_length=60, blank=False, null=True)
    title_two = models.CharField(max_length=60, blank=True, null=True)
    title_three = models.CharField(max_length=60, blank=True, null=True)
    title_four = models.CharField(max_length=60, blank=True, null=True)
    x_url = models.URLField()
    f_url = models.URLField()
    ig_url = models.URLField()
    linkedin_url = models.URLField()

    
class Service(models.Model):
    icon = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    description = RichTextField()

    def __str__(self):
        return self.title

        