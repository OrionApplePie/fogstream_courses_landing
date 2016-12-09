from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    """
    Model for feedback form
    """
    name = forms.CharField(label="Ваше имя:", widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    subject = forms.CharField(label="Тема", required=False,
                              widget=forms.TextInput(attrs={'placeholder': 'Тема (не обязательно)'}))
    email = forms.EmailField(label="Ваш e-mail")
    message = forms.CharField(label="Сообщение", widget=forms.Textarea(attrs={'placeholder': 'напишите Ваш вопрос'}))

    class Meta:
        model = Feedback
        fields = ('name', 'subject', 'email', 'message', )
