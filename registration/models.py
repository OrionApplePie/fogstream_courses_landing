from django.db import models
from courses.models import Courses


class Party(models.Model):
    party_name = models.CharField(max_length=200, verbose_name='Имя')
    party_fullname = models.CharField(max_length=200, verbose_name='Фамилия')
    party_email = models.CharField(max_length=200, verbose_name='Элекронная почта')
    party_login = models.CharField(max_length=200, default=" ", verbose_name='Логин')
    party_password = models.CharField(max_length=200, default=' ', verbose_name='Пароль')
    party_courses = models.ForeignKey(Courses)
    party_phone = models.CharField(max_length=200, verbose_name='Пароль')

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __unicode__(self):
        return self.party_login
