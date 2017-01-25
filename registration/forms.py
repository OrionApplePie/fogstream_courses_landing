from django import forms
from django.contrib.auth.models import User
from django.core import validators


class UserForm(forms.ModelForm):
    email = forms.EmailField(label='email', validators=[validators.EmailValidator])
    first_name = forms.CharField(label='Имя', validators=[validators.MaxLengthValidator(32)])
    last_name = forms.CharField(label='Фамилия', validators=[validators.MaxLengthValidator(32)])

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)


class ChangePassword(forms.Form):
        old_password = forms.CharField(label='Старый пароль')
        password1 = forms.CharField(label='Новый пароль')
        password2 = forms.CharField(label='Повтор пароля')


class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label="Email или логин", max_length=254)


class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    MIN_LENGTH = 8
    error_messages = {
        'password_mismatch': "пароли не совпадают.",
        'length_mismatch': "Длина пароля должна быть не менее %d символов." % MIN_LENGTH,
        }
    new_password1 = forms.CharField(label="Новый пароль",
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Подтвердите пароль",
                                    widget=forms.PasswordInput)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                    )
            if len(password2) < self.MIN_LENGTH:
                raise forms.ValidationError(
                    self.error_messages['length_mismatch'],
                    code='length_mismatch',
                )
        return password2

