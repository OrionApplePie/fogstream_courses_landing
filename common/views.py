from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import auth
from django.http import JsonResponse, HttpResponse

from common.models import HeadCarouselPicture, TeamMember
from .forms import FeedbackForm
from gallery.views import photo_list
from fc_landing.settings import DEFAULT_FROM_EMAIL


def index(request):
    """
    Main view for index page
    """
    context = {}
    head_pictures = HeadCarouselPicture.objects.order_by("priority")
    team = TeamMember.objects.order_by("id")
    context.update({'head_pictures': head_pictures, 'team': team})

    form = FeedbackForm()

    context.update({'form': form, 'username': auth.get_user(request).username})
    context.update(photo_list())
    return render(request, 'index.html', context)


def contact(request):
    """
    View for Feedback form, used in AJAX script /contactform/contactform.js

    """
    if request.method == 'POST':
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            form.save()
            contact_mail = request.POST.get('email', '')

            #TODO  Разные способ передачи именованных аргументов в EmailMessage - с именами и без
            email = EmailMessage(
                subject="Курсы Python/Django",
                body='Ваше сообщение отправлено, Спасибо!',
                from_email=DEFAULT_FROM_EMAIL,
                to=[contact_mail],
                headers={'Reply-To': contact_mail},
                reply_to=[contact_mail]
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
    return redirect('index')
