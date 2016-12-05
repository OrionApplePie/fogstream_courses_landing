from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from gallery import views
from registration.views import registration, profile, out

from common.views import contact
from coolapp.views import cool


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^', include('common.urls')),
    url(r'^$', views.photo_list),
    url(r'^registration/', registration),
    url(r'^out/', out),
    url(r'^profile/', profile)
    url(r'^$', include('common.urls')),
    url(r'^contact/', contact),
    url(r'^coolapp/', cool),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
