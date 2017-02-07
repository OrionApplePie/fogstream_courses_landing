from django.contrib.auth.models import User
from django.db import models
import datetime


class UserProfile(models.Model):
    """
    model for user profile. Need for relationship between user ans course.
    And maybe for adding some fields later
    """
    user = models.OneToOneField(User)
    course = models.CharField(max_length=200, verbose_name='Название курса', default=None)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural=u'User profile'


class UserRegisterConfirm(models.Model):
    """
    Model for sending email to user before registration
    Keeps activation key to create confirming url
    and key_expires, because key isn't eternal
    """
    email = models.EmailField(verbose_name='Email')
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())




