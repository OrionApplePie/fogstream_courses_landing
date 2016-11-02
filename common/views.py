from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def index(request):
    t = get_template('common/index.html')
    c = Context({})
    html = t.render(c)
    return HttpResponse(html)


def input_form(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)