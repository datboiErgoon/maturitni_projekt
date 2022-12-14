from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


class Genre(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True, default='')

    def __str__(self):
        return self.name


class Playlist(models.Model):
    playlistName = models.CharField(max_length=100)
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='album_images/', default='blank-playlist-picture.png')
    created_at = models.DateTimeField(default=datetime.now)
    caption = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.playlistName


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images/', default='cd.png')
    song = models.FileField(upload_to="post_songs/")
    title = models.CharField(max_length=255, default='unknown')
    trackNumber = models.IntegerField(max_length=255, blank=True, null=True, default=0)
    runtime = models.IntegerField(max_length=255, blank=True, null=True, default=0)
    lyrics = models.TextField(blank=True, null=True)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Post'

    def __str__(self):
        return f"Post - user:{self.user}, title: {self.title}"


class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
