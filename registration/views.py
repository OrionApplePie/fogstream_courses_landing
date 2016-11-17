from django.shortcuts import render
from courses.models import Courses


def registration(request):
    queryset = Courses.objects.all()
    context = {
        'courses': queryset
    }
    return render(request, 'registration/registration.html', context)
