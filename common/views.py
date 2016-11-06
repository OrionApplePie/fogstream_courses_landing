from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def index(request):
    template = get_template('index.html')
    context = Context({})
    html = template.render(context)
    return HttpResponse(html)


 #  this comment created from branch 'feedback'