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


