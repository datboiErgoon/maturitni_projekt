from django import forms
from .models import Songs


class UploadMP3Form(forms.ModelForm):
    class Meta:
        model = Songs
        fields = ['songfile']