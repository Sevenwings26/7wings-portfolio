from django.contrib import admin
from django.http import HttpRequest
from .models import GeneralInfo, Service, Frontendskill, Backend_dataskill, Portfolio

# Register your models here.
@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ['brand_name', 'name', 'phone', 'title_one']

    # # to remove pemission 
    # def has_add_permission(self, request, obj=None):
    #     return False
    
    # # to remove delete 
    # def has_delete_permission(self, request, obj=None):
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False
    

admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Frontendskill)
admin.site.register(Backend_dataskill)
