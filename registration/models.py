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


class Party(models.Model):
    party_name = models.CharField(max_length=200, verbose_name='Имя')
    party_fullname = models.CharField(max_length=200, verbose_name='Фамилия')
    party_email = models.CharField(max_length=200, verbose_name='Элекронная почта')
    party_password = models.CharField(max_length=200, default=' ', verbose_name='Пароль')
    party_courses = models.ForeignKey(Courses)
    party_phone = models.CharField(max_length=200, verbose_name='Телефон')
    party_entry = models.NullBooleanField(default=False)

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __unicode__(self):
        return self.party_login

