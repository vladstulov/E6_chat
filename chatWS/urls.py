from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.core.cache.backends.locmem import _caches as cache

from appchat.views import index


urlpatterns = [
    path('', index),
    path('appchat/', include('appchat.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if cache and cache.get('us', None):
    cache['my_cache'].clear()

