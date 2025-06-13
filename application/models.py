from django.db import models
from ckeditor.fields import RichTextField
from django_summernote.fields import SummernoteTextField


# Create your models here.
class GeneralInfo(models.Model):
    brand_name = models.CharField(max_length=60)
    first_name = models.CharField(max_length=60, default="Iyanu") # Update - 9th June, 2025
    last_name = models.CharField(max_length=60, default="Arowosola") # Update - 9th June, 2025
    phone = models.CharField(max_length=25)
    resume_link =  models.URLField(default='https://drive.google.com/drive/folders/1csFCVIVj7sSqbnHXLAR2K75Md36XYbeB')
    description = models.TextField(blank=True)
    email = models.EmailField(default='iarowosola@yahoo.com')
    address = models.CharField(max_length=100, blank=True, default='location')
    title_one = models.CharField(max_length=60, blank=False, null=True)
    title_two = models.CharField(max_length=60, blank=True, null=True)
    title_three = models.CharField(max_length=60, blank=True, null=True)
    title_four = models.CharField(max_length=60, blank=True, null=True)
    x_url = models.URLField()
    f_url = models.URLField()
    ig_url = models.URLField(blank=True)
    linkedin_url = models.URLField()
    github_url = models.URLField(default="https//:github.com/Sevenwings26")

    # add for more variables 
    birthday = models.CharField(max_length=20, blank=True, default='text')
    degree = models.CharField(max_length=150, blank=True, default='text')
    job_type = models.CharField(max_length=150, blank=True, default='text')
    location = models.CharField(max_length=150, blank=True, default='text')
    
    brief_bio = RichTextField(blank=False, default='text') # RichtextField
    bio = RichTextField(blank=False, default='text') # RichtextField
    # bio = SummernoteTextField(blank=False, default='text') # RichtextField

    # update models - 6th June, 2025.
    about_title = models.CharField(max_length=200, blank=True, default='text')
    hero_caption = models.TextField(default="")
    service_caption = models.TextField(blank=True)


    
    def __str__(self):
        return self.first_name


class Service(models.Model):
    icon = models.CharField(max_length=60, blank=True)
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=100, default="service")
    image = models.ImageField(upload_to='service-images/', blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    # description = SummernoteTextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)

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


class Portfolio(models.Model):
    p_title = models.CharField(max_length=300)
    p_description = models.TextField()
    p_image = models.ImageField(upload_to="portfolio/")
    live_link = models.URLField(blank=True)

    def __str__(self):
        return f"{self.p_title} - {self.p_description}"

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

