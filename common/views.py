from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import auth
from django.http import JsonResponse

from .forms import FeedbackForm

from .models import HeadPicture, OurTeam


#  this comment created from branch 'feedback'

def index(request):
    """
    Main view for index page
    """
    context = {}
    HeadPictures = HeadPicture.objects.order_by("priority")
    Team = OurTeam.objects.order_by("id")
    context.update({'HeadPictures': HeadPictures, 'Team': Team})
    form = FeedbackForm()
    context.update({'form': form, 'username': auth.get_user(request).username})
    return render(request, 'index.html', context)


def contact(request):
    """
    View for Feedback form, used in AJAX script /contactform/contactform.js

    """
    if request.method == 'POST':
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            form.save()
            contact_name = request.POST.get('name', '')
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
    return redirect('/') # if just go to www.host.com/contact without form

