from django.db import models


def song_path(instance, filename):
    return 'media/' + str(instance.id) + '/attachments/' + filename




class Songs(models.Model):
    songfile = models.FileField(upload_to=song_path, verbose_name='MP3 File', help_text='Upload your song')
    album = models.CharField(max_length=100, verbose_name='Name of the album', help_text='Enter the name of the album')
    title = models.CharField(max_length=100, verbose_name='Name of the song', help_text='Enter the name of the song')
    artist = models.CharField(max_length=100, verbose_name='Name of the artist',
                              help_text='Enter the name of the artist')
    tracktotal = models.IntegerField(verbose_name='Total number of tracks on the album',
                                     help_text='Enter the total number of tracks on the album')
    date = models.IntegerField(verbose_name='Year of the albums release',
                               help_text='Enter the year of the albums release')
    tracknumber = models.IntegerField(verbose_name='Track number', help_text='Enter the track number')
    filetype = models.CharField(max_length=20, verbose_name='File type', help_text='Enter the file type')
    runtime = models.IntegerField(verbose_name='Full length of the song',
                                         help_text='Enter the full length of the song')
    genre = models.CharField(max_length=100, verbose_name='Genre', help_text='Enter the genre')
    disc = models.IntegerField(verbose_name='Total number of discs', help_text='Enter the total number of discs')
    lyrics = models.CharField(max_length=500, verbose_name='Lyrics', help_text='Enter the lyrics')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


# Create your models here.

