from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(label="Ваше имя:",
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя',
                                                         'data-rule': 'minlen:4',
                                                         'data-msg': 'Please enter at least 4 chars'}))
    subject = forms.CharField(label="Тема", required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тема',
                                                            'data-msg': 'Please enter at least 8 chars of subject'}))
    email = forms.EmailField(label="Ваш e-mail",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш e-mail',
                                                           'data-rule': 'email',
                                                           'data-msg': 'Please enter a valid email'}))
    message = forms.CharField(label="Сообщение",
                              widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5',
                                                           'data-rule': 'required',
                                                           'data-msg': 'Please write something for us'}))

    class Meta:

        model = Feedback
        fields = ('name', 'subject', 'email', 'message', )
