from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import auth
from django.http import JsonResponse

from .forms import FeedbackForm

from .models import HeadPicture, OurTeam

# вот эти две хуиты исправить в одну
def index(request):
    HeadPictures = HeadPicture.objects.order_by("priority")
    Team = OurTeam.objects.order_by("id")
    context = {'HeadPictures': HeadPictures, 'Team': Team}
    return render(request, 'common/index.html', context)


 #  this comment created from branch 'feedback'

def index(request):
    """
    Main view for index page
    """
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'form': form})
    else:
        form = FeedbackForm()
    return render(request, 'index.html', {'form': form, 'username': auth.get_user(request).username})


def contact(request):
    """
    View for FeedBack form, used in AJAX script /contactform/contactform.js

    """
    if request.method == 'POST':
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            form.save()
            contact_mail = request.POST.get('email', '')
            email = EmailMessage(
                "Курсы Python/Django",
                "Ваше сообщение отправлено, Спасибо!",
                "from@example.com",
                [contact_mail],
                reply_to=['example@example.ru'],
                headers={'Reply-To': contact_mail}
            )
            email.send()
            data = {
                'result': 'success',
                'message': 'Ваше сообщение отправлено!'
            }
            return JsonResponse(data)
        else:
            response = {}
            for k in form.errors:
                response[k] = form.errors[k][0]
                data = {'response': response,
                    'result': 'error',
                    'message': 'Form invalid!',
                    }
            return JsonResponse(data)
    return redirect('/')

