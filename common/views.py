from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context, loader
from django.http import HttpResponse
from common.forms import FeedbackForm

from .models import HeadPicture, OurTeam

def index(request):
    HeadPictures = HeadPicture.objects.order_by("priority")
    Team = OurTeam.objects.order_by("id")
    context = {'HeadPictures': HeadPictures, 'Team': Team}
    return render(request, 'common/index.html', context)


 #  this comment created from branch 'feedback'

def home(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'form': form})
    else:
        form = FeedbackForm()
    return render(request, 'index.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            # send_mail(
            #     cd['subject'],
            #     cd['message'],
            #     cd.get('email', 'noreply@example.com'),
            #     ['siteowner@example.com'],
            #     fail_silently=False,
            # )
        return HttpResponse('send successfully')

    else:
        return HttpResponse('error')