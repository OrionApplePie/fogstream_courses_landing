from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context, loader
from django.http import HttpResponse
from .forms import FeedbackForm


def index(request):
    template = get_template('index.html')
    context = Context({})
    html = template.render(context)
    return HttpResponse(html)


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