from django.contrib import admin

# Register your models here.
from .models import CustomUser

# admin.site.register(CustomUser)

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "first_name", "last_name", "email"
    ]
    