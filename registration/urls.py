from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from registration.views import login, profile, logout, send_registration_email, registration_confirm
from .views import ResetPasswordRequestView, PasswordResetConfirmView


urlpatterns = [
    url(r'^login/', login),
    url(r'^logout/', logout),
    url(r'^profile/', profile),
    url(r'^registration/', send_registration_email),
    url(r'^confirm/(\w+)/', registration_confirm),

    url(r'^reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),
        name='reset_password_confirm'),
    url(r'^reset_password', ResetPasswordRequestView.as_view())


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
