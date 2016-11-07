from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False)
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=32,blank=True, null=True)
    message = models.CharField(max_length=255, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    answer = models.TextField(default='')

    def __str__(self):
        return self.name
'''test'''
# Create your models here.

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




