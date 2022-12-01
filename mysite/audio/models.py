from django.db import models

class Songs(models.Model):
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
    length_seconds = models.IntegerField(verbose_name='Full length of the song',
                                         help_text='Enter the full length of the song')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


# Create your models here.

