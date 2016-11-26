from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from common.views import contact
from coolapp.views import cool


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^$', include('common.urls')),
    url(r'^contact/', contact),
    url(r'^coolapp/', cool),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
