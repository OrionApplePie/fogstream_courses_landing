import random

from django.shortcuts import render
from .models import Photo


def photo_list(request):
    queryset = Photo.objects.all()
    if len(list(queryset)) < 9:
        img_list = random.sample(list(queryset), len(list(queryset)))
    else:
        img_list = random.sample(list(queryset), 9)
    context = {
        'photos': queryset,
        'img_list': img_list,
    }
    return render(request, 'index.html', context)
