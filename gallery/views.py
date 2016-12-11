import random

from .models import Photo, Album


def photo_list():
    """
    Функция генерирует из базы 9 случайных фотографий
    передает их в контекст вместе с альбомом фотографий
    :return: контекст
    """
    queryset_photo = Photo.objects.all()
    queryset_album = Album.objects.all()
    if len(list(queryset_photo)) < 9:
        img_list = random.sample(list(queryset_photo), len(list(queryset_photo)))
    else:
        img_list = random.sample(list(queryset_photo), 9)
    context = {
        'photos': queryset_photo,
        'img_list': img_list,
        'albums': queryset_album,
    }
    return context
