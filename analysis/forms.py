from django.contrib.auth.models import User
from django.forms import ModelForm, Form
from django import forms
class Sentiment(forms.Form):
   text = forms.CharField()