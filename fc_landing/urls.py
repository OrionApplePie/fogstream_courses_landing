from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from registration.views import registration, profile, out


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^registration/', registration),
    url(r'^out/', out),
    url(r'^profile/', profile),
    url(r'^', include('common.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
