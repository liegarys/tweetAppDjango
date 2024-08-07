from django import forms
from tweetapp.models import Tweet
from django.forms import ModelForm


class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(max_length=50, label="Nickname")
    message_input = forms.CharField(max_length=100, label= "Message")


class AddTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ["nickname", "message"]
