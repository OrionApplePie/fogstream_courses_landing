from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

from .models import HeadPicture, OurTeam

def index(request):
    HeadPictures = HeadPicture.objects.order_by("priority")
    Team = OurTeam.objects.order_by("id")
    context = {'HeadPictures': HeadPictures, 'Team': Team}
    return render(request, 'common/index.html', context)


 #  this comment created from branch 'feedback'