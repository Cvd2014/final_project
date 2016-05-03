from django import forms
from models import Message
from django.forms import ModelForm

class ContactForm(ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Message
        fields = ('sender', 'subject', 'message', 'email')