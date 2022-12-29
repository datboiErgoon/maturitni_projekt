import os

from django.core.files.storage import default_storage

from .models import Post
from django import forms
from django.conf import settings


class UploadSongForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['song']


# def file_upload(request):
#     save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', request.FILES['file'])
#     path = default_storage.save(save_path, request.FILES['file'])
#     return default_storage.path(path)
