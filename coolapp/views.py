from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def cool(request):
    return HttpResponse("hello, this is example App!")
