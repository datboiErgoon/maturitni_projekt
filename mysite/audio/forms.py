from django import forms


class UploadMP3Form(forms.Form):
    file = forms.FileField()
