# Generated by Django 4.1.3 on 2022-12-30 16:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='genre',
        ),
        migrations.AddField(
            model_name='playlist',
            name='caption',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playlist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='playlist',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='player.genre'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='image',
            field=models.ImageField(default='blank-album-picture.jpg', upload_to='album_images/'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='no_of_likes',
            field=models.IntegerField(default=0),
        ),
    ]
