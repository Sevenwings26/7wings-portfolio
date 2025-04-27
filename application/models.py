from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class GeneralInfo(models.Model):
    brand_name = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    email = models.EmailField(default='mail@mail.com', blank=True)
    address = models.CharField(max_length=100, blank=True, default='location')
    title_one = models.CharField(max_length=60, blank=False, null=True)
    title_two = models.CharField(max_length=60, blank=True, null=True)
    title_three = models.CharField(max_length=60, blank=True, null=True)
    title_four = models.CharField(max_length=60, blank=True, null=True)
    x_url = models.URLField()
    f_url = models.URLField()
    ig_url = models.URLField()
    linkedin_url = models.URLField()
    github_url = models.URLField(default="https//:github.com")

    # add for more variables 
    about_title = models.CharField(max_length=200, blank=True, default='text')
    birthday = models.CharField(max_length=20, blank=True, default='text')
    degree = models.CharField(max_length=150, blank=True, default='text')
    job_type = models.CharField(max_length=150, blank=True, default='text')
    location = models.CharField(max_length=150, blank=True, default='text')
    bio = RichTextField(blank=False, default='text')


    
class Service(models.Model):
    icon = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    image = models.ImageField(upload_to='service-images/', blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title


# skills set1 
class Frontendskill(models.Model):
    skill = models.CharField(max_length=150, blank=True)
    percentage = models.CharField(max_length=15, blank=True)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.skill}: {self.percentage}"

class Backend_dataskill(models.Model):
    skill = models.CharField(max_length=150, blank=True)
    percentage = models.CharField(max_length=15, blank=True)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.skill}: {self.percentage}"


# Contact Logs - number of times a particular user sent mail 
class ContactFormLog(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    sent_time = models.DateTimeField(null=True, blank=True)
    is_success = models.BooleanField(default=False)
    is_error = models.BooleanField(default=False)
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

