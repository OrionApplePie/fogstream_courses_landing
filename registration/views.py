# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from django.core.mail import send_mail
from django.contrib import auth
from django.utils import timezone
import hashlib
import datetime
import random

from registration.models import UserProfile, UserRegisterConfirm
from courses.models import Courses


def send_registration_email(request):
    queryset = Courses.objects.all()
    context = {
        'courses': queryset,
    }
    if request.POST:
        email = request.POST.get('email', '')
        if User.objects.filter(email=email).exists():
            messages.error(request, u'Введенный электронный адрес уже занят')
        if email:
            arg = str(random.random()).encode('utf-8')
            salt = hashlib.sha1(arg).hexdigest()[:5]
            arg = str(salt + email).encode('utf-8')
            activation_key = hashlib.sha1(arg).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            user_reg_confirm = UserRegisterConfirm(email=email, activation_key=activation_key,
                                                   key_expires=key_expires)
            user_reg_confirm.save()
            subject = u"Fogstream courses Подтверждение регистрации"
            message = u"Спасибо за регистрацию! Ссылка для подтверждения: " \
                      "http://127.0.0.1:8000/auth/confirm/{0}".format(activation_key)
            send_mail(subject, message, 'myemail@example.com', (email,), fail_silently=False)
            return render_to_response('registration/confirm_sending.html')
    return render(request, 'registration/registration.html', context)


def registration_confirm(request, activation_key):
    if request.user.is_authenticated():
        return redirect('/')
    user_reg_confirm = get_object_or_404(UserRegisterConfirm,
                                         activation_key=activation_key)
    print(timezone.now())
    print(user_reg_confirm.key_expires)
    if user_reg_confirm.key_expires < timezone.now():
        return render_to_response('registration/confirm_expired.html')
    else:
        queryset = Courses.objects.all()
        context = {
            'courses': queryset,
        }
        if request.POST:
            username = request.POST.get('username', '')
            if User.objects.filter(username=username).exists():
                messages.error(request, u'Введенный логин уже занят')
            course = request.POST.get('course', '')
            email = user_reg_confirm.email
            password = request.POST.get('password', '')
            password_confirm = request.POST.get('password_confirm', '')
            if password == password_confirm and len(password) >= 8:
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()
                user_profile = UserProfile(user=user, course=course)
                user_profile.save()
                messages.success(request, u'Регистрация прошла успешно. Вы можете войти в личный кабинет')
                UserRegisterConfirm.objects.filter(activation_key=activation_key).delete()
                return redirect('/auth/login/')
            else:
                messages.error(request, u"Пожалуйста, введите совпадающие пароли длиной от 8 символов")
        return render(request, 'registration/registration_continue.html', context)


def login(request):
    """
    Функция авторизации пользователя

    """
    queryset = Courses.objects.all()
    context = {
        'courses': queryset,
        'auth': auth.get_user(request)
    }
    if request.POST:
        username = request.POST.get('login', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            context['login_error'] = "Пользователь не найден"
            return render(request, 'registration/login.html', context)
    else:
        return render(request, 'registration/login.html', context)


def registration(request):
    queryset = Courses.objects.all()
    context = {
        'courses': queryset,
    }
    return render(request, 'registration/registration.html', context)


def password_authentication(password):
    """
    Функция проверки пороля(состоит ли он и из цифр и из букв)
    :param password: пароль для проверки
    :return:True - если пароль соответствует требованиям, False - в противном случае
    """
    if not password.isdigit() and not password.isalpha():
        return True
    else:
        return False


def profile(request):
    """
    Функция изменения данныхв личном кабинете

    """
    fail = False
    context = {
        'auth': auth.get_user(request),
        'error': '',
    }
    if request.POST:
        user = auth.get_user(request)
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        old_password = request.POST.get('old_password', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        username = request.POST.get('login', '')
        if username:
            user.username = username
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if email:
            user.email = email
        if old_password and password1 and password2:
            if not user.check_password(old_password):
                fail = True
                context['error'] = 'Старый пароль неверный'

            if password1 != password2:
                fail = True
                context['error'] = 'Новые пароли не совпадают'
            if len(password2) < 8:
                fail = True
                context['error'] = 'Пароль должен состоять из восьми и более символов'
            if password_authentication(password1) == False:
                fail = True
                context['error'] = 'Пароль должен состоять из цифр и букв'
            if user.check_password(old_password) and password1 == password2 and len(
                    password2) >= 8 and password_authentication(password1):
                user.set_password(password1)
                auth.login(request, user)
        user.save()
        if not fail:
            context['error'] = 'Сохранено'
        return render(request, 'registration/profile.html', context)
    else:
        return render(request, 'registration/profile.html', context)


def logout(request):

    """
    Функция выхода

    """
    auth.logout(request)
    return redirect('/')
