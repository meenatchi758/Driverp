# mydashboard/urls.py
from django.contrib import admin
from django.urls import path, include   # ✅ import path + include
from django.conf import settings        # ✅ import settings
from django.conf.urls.static import static  # ✅ for serving media in dev

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("drive.urls")),   # ✅ include app urls
]

# ✅ Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)