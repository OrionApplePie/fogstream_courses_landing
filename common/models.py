from django.db import models
from django.core import validators


max_len_validate = validators.MaxLengthValidator(32);

class Feedback(models.Model):
    """
    Model for feedback questions. Contain field 'Answer' for answer.
    """
    name = models.CharField(max_length=32, verbose_name='Имя', validators=[max_len_validate])
    email = models.EmailField(verbose_name='e-mail', validators=[validators.validate_email])
    subject = models.CharField(max_length=32, blank=True, verbose_name='Тема')
    message = models.CharField(max_length=255, verbose_name='Сообщение',
                               validators=[validators.MaxLengthValidator(255)])
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата и время')
    answer = models.TextField(verbose_name='Ответ')
    is_reply = models.BooleanField(default=False, verbose_name='Отвечено')

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.name


class HeadPicture(models.Model):
    title = models.CharField(max_length=255, null=True)
    interval = models.IntegerField(default=5000,null=False)
    priority = models.IntegerField(primary_key=True, unique=True)
    image = models.ImageField(upload_to='head/')
    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url)
        else:
            return '(Нет изображения)'
    image_img.allow_tags = True


class OurTeam(models.Model):
    name = models.CharField(max_length=200, null=False)
    position = models.CharField(max_length=200, null=False)
    photo = models.ImageField(upload_to='team/')
    def image_img(self):
        if self.photo:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.photo.url)
        else:
            return '(Нет изображения)'
    image_img.allow_tags = True





