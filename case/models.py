from django.db import models
# from ckeditor.fields import RichTextField
from django_prose_editor.fields import ProseEditorField

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = ProseEditorField()
    # body = RichTextField(default="Service details")
    body = ProseEditorField(default="Service details")

    def __str__(self):
        return self.title


# not useful 
class ServiceFeature(models.Model):
    service = models.ForeignKey(Service, related_name='features', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)


# clients testimony
class Testimonial(models.Model):
    client_image= models.ImageField(upload_to='clients/')
    client_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    # body = RichTextField()
    body = ProseEditorField()

    # def imageURL:

    def __str__(self):
        return f"{client_name} - {company_name}"


