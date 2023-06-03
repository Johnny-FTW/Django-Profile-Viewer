from django import forms
from django.forms import ModelForm

from chat.models import ChatMessage


class ChatMessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control type_msg", "placeholder":"Type your message..."}))

    class Meta:
        model = ChatMessage
        fields = ["body",]