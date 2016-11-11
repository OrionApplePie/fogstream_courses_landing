from django.db import models


class Courses(models.Model):
    courses_name_course = models.CharField(max_length=200, verbose_name='Название')
    courses_date_begin = models.DateField(verbose_name='Дата начала')
    courses_date_end = models.DateField(verbose_name='Дата окончания')


    class Meta:
        ordering = ['courses_name_course']
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'



    def __unicode__(self):
        return self.courses_name_course


class Party(models.Model):
    party_name = models.CharField(max_length=200, verbose_name='Имя')
    party_fullname = models.CharField(max_length=200, verbose_name='Фамилия')
    party_email = models.CharField(max_length=200, verbose_name='Элекронная почта')
    party_login = models.CharField(max_length=200, default=" ", verbose_name='Логин')
    party_password = models.CharField(max_length=200, default=' ', verbose_name='Пароль')
    party_courses = models.ForeignKey(Courses)

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __unicode__(self):
        return self.party_login
