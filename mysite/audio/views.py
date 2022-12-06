from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .getsonginfo import loadfile
from .forms import UploadMP3Form
from django.http import HttpResponseRedirect
from .models import Songs
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def index(request):

    context = {
        'songs': Songs.objects.order_by('title')
    }
    return render(request, 'base.html', context=context)

def loadMP3(request):
    if request.method == 'POST':
        form = UploadMP3Form(request.POST)
        if form.is_valid():
            try:
                song = Songs()
                songinfo = loadfile(form)
                # song.title = songinfo['TIT2']
                # song.artist = songinfo['TPE1']
                # song.album = songinfo['TALB']
                # song.genre = songinfo['TCON']
                # song.track_number = songinfo['TRCK']
                # song.disc = songinfo['TPOS']
                # song.year = songinfo['TDRC']
                # song.runtime = songinfo.info.length
                # song.lyrics = songinfo['"USLT::XXX"']
                song.songfile = form
                song.title = songinfo[0]
                song.artist = songinfo[1]
                song.album = songinfo[2]
                song.genre = songinfo[3]
                song.tracknumber = songinfo[4]
                song.disc = songinfo[5]
                song.date = songinfo[6]
                song.runtime = songinfo[7]
                song.lyrics = songinfo[9]
                song.save()
            except:
                return redirect('song_list')


class SongListView(ListView):
    model = Songs
    context_object_name = 'song_list'
    template_name = 'player/list.html'

    def get_queryset(self):
        return Songs.objects.all()



class SongDetailView(DetailView):
    model = Songs
    context_object_name = 'song_detail'
    template_name = 'player/detail.html'



class SongCreate(CreateView):
    model = Songs
    template_name = 'player/uploadmp3.html'
    form_class = UploadMP3Form

    def get_success_url(self):
        return reverse_lazy('song_detail', kwargs={'pk' : self.object.pk})