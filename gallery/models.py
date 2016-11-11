from django.db import models


class Album(models.Model):
    album_title = models.CharField(max_length=100, verbose_name='Название')
    album_slug = models.SlugField(max_length=100, unique=True, verbose_name='Описание')

    class Meta:
        ordering = ['album_title']
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __unicode__(self):
        return self.album_title


class Photo(models.Model):
    photo_title = models.CharField(max_length=200, verbose_name='Название')
    photo_album = models.ForeignKey(Album, verbose_name='Альбом')
    img = models.ImageField('Photo', upload_to='images')

    def image_img(self):
        if self.img:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.img.url)
        else:
            return '(Нет изображения)'
    image_img.allow_tags = True

    class Meta:
        ordering = ['photo_title']
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

    def __unicode__(self):
        return self.photo_title
