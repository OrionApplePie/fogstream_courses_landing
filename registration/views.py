from django.shortcuts import render_to_response, redirect, render
from courses.models import Courses
from django.contrib import auth
from django.contrib.auth.models import User


def registration(request):
    queryset = Courses.objects.all()
    context = {
        'courses': queryset,
        'auth': auth.get_user(request)
    }
    if request.POST:
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            # render(request, 'registration/registration.html')
            return redirect('/')
        else:
            context['login_error'] = "Пользователь не найден"
            return render(request, 'registration/registration.html', context)
    else:
        return render(request, 'registration/registration.html', context)


def profile(request):
    text = ''
    context = {
        'auth': auth.get_user(request)
    }
    if request.POST:
        user = auth.get_user(request)
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        old_password = request.POST.get('old_password', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        if first_name != '':
            user.first_name = first_name
            user.save()
        if last_name != '':
            user.last_name = last_name
            user.save()
        if email != '':
            user.email = email
            user.save()
        if old_password != '' and password1 != '' and password2 != '':
            if user.check_password(old_password) and password1 == password2:
                user.set_password(password1)
                user.save()
                context['login_error'] = 'save'
            else:
                context['login_error'] = "старый пароль неверный или новые пароли не совпадают"
        context['login_error'] = 'save'
        return render(request, 'registration/profile.html', context)
    else:
        return render(request, 'registration/profile.html', context)

def out(request):
    auth.logout(request)
    return redirect('/')
