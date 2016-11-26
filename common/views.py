from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context, loader
from django.http import HttpResponse
from .forms import FeedbackForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib import auth


def home(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'form': form})
    else:
        form = FeedbackForm()
    return render(request, 'index.html', {'form': form, 'username': auth.get_user(request).username})


def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            form.save()
            contact_name = request.POST.get('name', '')
            contact_mail = request.POST.get('email', '')
            email = EmailMessage(
                "Курсы Python/Django",
                "Ваше сообщение отправлено, спасибо!",
                "from@example.com",
                [contact_mail],
                reply_to=['example@example.ru'],
                headers={'Reply-To': contact_mail}
            )
            email.send()

            #send_mail(
             #   'Курсы Python/Django',
              #  'Ваше сообщение отправлено, спасибо!',
               # 'cauchy.acc@gmail.com',
               # [form.email],
                #fail_silently=False,
            #)
        return HttpResponse('send successfully')

    else:
        return HttpResponse('error')