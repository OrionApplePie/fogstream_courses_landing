from django.conf.urls import url, include
from django.contrib import auth
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import password_reset
from registration.views import login, profile, logout, send_registration_email, registration_confirm
from django.contrib import admin
from .views import ResetPasswordRequestView, PasswordResetConfirmView


urlpatterns = [
    url(r'^login/', login),
    url(r'^logout/', logout),
    url(r'^profile/', profile),
    url(r'^registration/', send_registration_email),
    url(r'^confirm/(\w+)/', registration_confirm),

    url(r'^account/reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    PasswordResetConfirmView.as_view(), name='reset_password_confirm'),
    # PS: url above is going to used for next section of
    # implementation.
    url(r'^account/reset_password',
    ResetPasswordRequestView.as_view())


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
    url(r'^password/reset/$', auth.views.password_reset, {'post_reset_redirect': '/auth/password/reset/done/'},
        name='password_reset'),
    url(r'^password/reset/done/$', auth.views.password_reset_done),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth.views.password_reset_confirm, {'post_reset_redirect': '/auth/password/done/'},
        name='password_reset_confirm'),
    url(r'^password/done/$', auth.views.password_reset_complete),
    """