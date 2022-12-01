from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .getsonginfo import loadfile
from .forms import UploadMP3Form
from django.http import HttpResponseRedirect


def index(request):
    return render(request, "base.html")

#def loadMP3(request):
    #if request.method == ["post"]