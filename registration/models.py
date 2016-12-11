from django.contrib.auth.models import User
from django.db import models
import datetime

from courses.models import Courses


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    course = models.CharField(max_length=200, verbose_name='Название курса', default=None)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural=u'User profile'


class UserRegisterConfirm(models.Model):
    email = models.EmailField(verbose_name='Email')
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())




