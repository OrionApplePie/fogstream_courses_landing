from django.conf.urls import url
from django.contrib import auth
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import password_reset

from . import views


urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout),
    url(r'^register/', views.register),
    url(r'^password/reset/$', auth.views.password_reset, {'post_reset_redirect': '/auth/password/reset/done/'},
        name='password_reset'),
    url(r'^password/reset/done/$', auth.views.password_reset_done),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth.views.password_reset_confirm, {'post_reset_redirect': '/auth/password/done/'},
        name='password_reset_confirm'),
    url(r'^password/done/$', auth.views.password_reset_complete),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
