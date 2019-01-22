from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path(r'^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$',
         RedirectView.as_view(url='/static/%(path)s', permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
