from django.db import models


class Course(models.Model):
    # не исправлены названия полей
    # TODO Модель для одного курса, а называется КурсЫ, во множ. числе
    course_name = models.CharField(max_length=200, verbose_name='Название')
    date_begin = models.DateField(verbose_name='Дата начала')
    date_end = models.DateField(verbose_name='Дата окончания')

    class Meta:
        ordering = ['course_name']
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __unicode__(self):
        return self.course_name


