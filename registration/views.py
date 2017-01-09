from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from django.contrib import auth
from django.utils import timezone

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.db.models.query_utils import Q
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template import loader
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.views.generic import *
from django.forms.utils import ErrorList

from django.contrib import messages
from django.contrib.auth.models import User

import hashlib
import datetime
import random

from fc_landing.settings import DEFAULT_FROM_EMAIL
from registration.models import UserProfile, UserRegisterConfirm
from courses.models import Courses
from .forms import PasswordResetRequestForm, SetPasswordForm, UserForm


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<div class="error">%s</div>' % e for e in self])


class ResetPasswordRequestView(FormView):
    # code for template is given below the view's code
    template_name = "registration/reset_template.html"
    success_url = '/auth/reset_password/'
    form_class = PasswordResetRequestForm

    @staticmethod
    def validate_email_address(email):

        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    # may be staticmethod
    def reset_password(self, user, request):
        context = {
            'email': user.email,
            'domain': request.META['HTTP_HOST'],
            'site_name': 'Курсы Django от Fogstream',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'user': user,
            'token': default_token_generator.make_token(user),
            'protocol': 'http',
        }
        subject_template_name = 'registration/password_reset_subject.txt'
        # copied from
        # django/contrib/admin/templates/registration/password_reset_subject.txt
        # to templates directory
        email_template_name = 'registration/password_reset_email.html'
        # copied from
        # django/contrib/admin/templates/registration/password_reset_email.html
        # to templates directory
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        email = loader.render_to_string(email_template_name, context)
        send_mail(subject, email, DEFAULT_FROM_EMAIL,
                  [user.email], fail_silently=False)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, error_class=DivErrorList)
        try:
            if form.is_valid():
                data = form.cleaned_data["email_or_username"]
            # uses the method written above
            if self.validate_email_address(data) is True:
                '''
                If the input is an valid email address,
                then the following code will lookup for users associated with that email address.
                If found then an email will be sent to the address, else an error message will be printed on the screen.
                '''
                associated_users = User.objects.filter(
                    Q(email=data) | Q(username=data))
                if associated_users.exists():
                    for user in associated_users:
                        self.reset_password(user, request)

                    result = self.form_valid(form)
                    messages.success(
                        request, 'Письмо отправлено на {0}.'
                                 ' Пожалуйста проверьте Ваш почтовый ящик для продолжения.'.format(data))
                    return result
                result = self.form_invalid(form)
                messages.error(
                    request, 'Пользователь с таким адресом электронной почты не найден')
                return result
            else:
                '''
                If the input is an username,
                then the following code will lookup for users associated with that user.
                If found then an email will be sent to the user's address,
                else an error message will be printed on the screen.
                '''
                associated_users = User.objects.filter(username=data)
                if associated_users.exists():
                    for user in associated_users:
                        self.reset_password(user, request)
                    result = self.form_valid(form)
                    messages.success(
                        request, "Письмо отправлено на адресс пользователя {0}."
                                 " Пожалуйста проверьте Ваш почтовый ящик для продолжения".format(data))
                    return result
                result = self.form_invalid(form)
                messages.error(
                    request, 'Пользователь с таким именем не найден.')
                return result
            messages.error(request, 'Ошибка ввода!')
        except Exception as e:
            print(e)
        return self.form_invalid(form)


class PasswordResetConfirmView(FormView):
    template_name = "registration/reset_template.html"
    success_url = '/auth/login/'
    form_class = SetPasswordForm

    def post(self, request, uidb64=None, token=None, *arg, **kwargs):
        """
        View that checks the hash in a password reset link and presents a
        form for entering a new password.
        """
        UserModel = get_user_model()
        form = self.form_class(request.POST, error_class=DivErrorList)
        assert uidb64 is not None and token is not None  # checked by URLconf
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            if form.is_valid():
                new_password = form.cleaned_data['new_password2']
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Пароль был изменен успешно.')
                return self.form_valid(form)
            else:
                #messages.error(
                 #   request, 'Произошла ошибка.')
                return self.form_invalid(form)
        else:
            messages.error(
                request, 'Ссылка сброса пароля не действительна.')
            return self.form_invalid(form)


def send_registration_email(request):
    """
    Функция отправляет на введенный пользователем емейл
    письмо с ссылкой для подтверждения регистрации.
    Ссылка генерируется случайно и записывается в activation_key
    В key_expires записывается дата истечения ключа
    """
    queryset = Courses.objects.all()
    context = {
        'courses': queryset,
    }
    if request.POST:
        email = request.POST.get('email', '')
        if email:

            if User.objects.filter(email=email).exists():
                messages.error(request, u'Введенный электронный адрес уже занят')
                context.update({'massages': messages})
                return render(request, 'registration/registration.html', context)
            else:
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
        else:
            messages.error(request, 'Введите email!')
            context.update({'massages': messages})
            return render(request, 'registration/registration.html', context)
    return render(request, 'registration/registration.html', context)


def registration_confirm(request, activation_key):
    """
    Функция ищет переданный activation_key в таблице. Если есть, происходит проверка
    по сроку истечения ключа. Если истек - перенаправляет на страницу, с которой
    пользователь может запросить новую ссылку. Если не истек - появляется форма, где
    пользователь вводит логин, пароль, подтверждение пароля и курс. Пароль не может
    быть длиной меньше 8 символов, а также состоять только из букв или только из
    цифр. После успешной регистрации появляется страница с авторизацией.
    """
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
            if password == password_confirm and len(password) >= 8 and password_authentication(password):
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()
                user_profile = UserProfile(user=user, course=course)
                user_profile.save()
                messages.success(request, u'Регистрация прошла успешно. Вы можете войти в личный кабинет')
                UserRegisterConfirm.objects.filter(activation_key=activation_key).delete()
                return redirect('/auth/login/')
            else:
                messages.error(request, u"Пожалуйста, введите совпадающие пароли длиной от 8 символов. "
                                        u"Пароль не должен содержать только цифры или только буквы.")
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
            return redirect('/')  # Что за редиректы на строковые урлы??
        else:
            context['login_error'] = "Пользователь не найден"
            return render(request, 'registration/login.html', context)
    else:
        return render(request, 'registration/login.html', context)


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


def profile2(request):
    context = {}
    user = User.objects.get(pk=auth.get_user(request).pk)
    if request.POST:

        form = UserForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/auth/profile2/')
        else:
            error = 'Введите корректные данные'
            #form = UserForm(instance=user)
            context.update({'form': form, 'username': auth.get_user(request).username, 'error': error})
            return render(request, 'registration/profile2.html', context)

    else:
        form = UserForm(instance=user)
        context.update({'form': form, 'username': auth.get_user(request).username, 'pk': auth.get_user(request).pk})
        return render(request, 'registration/profile2.html', context)


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
