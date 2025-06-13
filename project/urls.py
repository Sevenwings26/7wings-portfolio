"""
URL configuration for project project.
"""


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("application.urls")),
    path("", include("case.urls")),
    path("blog/", include("blog.urls")),
    path("account/", include("acct.urls")),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('summernote/', include('django_summernote.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

