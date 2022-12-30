from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from mutagen._util import loadfile
from mutagen.mp3 import MP3
from io import BytesIO
from PIL import Image
from .forms import UploadSongForm
from .models import Profile, Post, LikePost, FollowersCount, Playlist, Genre
from itertools import chain
import random

import mutagen


# Create your views here.

# user_posts = Post.objects.filter(user=user_object)
# album_posts = Post.objects.filter(playlist=)


def index(request):
    return render(request, 'index.html')


@login_required(login_url='signin')
def main(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    user_following_list = []
    feed = []

    user_following = FollowersCount.objects.filter(follower=request.user.username)

    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)

    feed_list = list(chain(*feed))

    # user suggestion starts
    all_users = User.objects.all()
    user_following_all = []

    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)

    new_suggestions_list = [x for x in list(all_users) if (x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(new_suggestions_list) if (x not in list(current_user))]
    random.shuffle(final_suggestions_list)

    username_profile = []
    username_profile_list = []

    for users in final_suggestions_list:
        username_profile.append(users.id)

    for ids in username_profile:
        profile_lists = Profile.objects.filter(id_user=ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))

    return render(request, 'base.html', {'user_profile': user_profile, 'posts': feed_list,
                                         'suggestions_username_profile_list': suggestions_username_profile_list[:4]})


@login_required(login_url='signin')
def upload_view(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    print("upload view")
    if request.method == 'POST':
        user = request.user.username
        db_user = User.objects.get(username=user)

        def add_song(myfile):
            fs = FileSystemStorage()
            filename = fs.save("post_songs/" + myfile.name, myfile)
            uploaded_file_url = fs.url(filename)

            file_addr = ("post_songs/" + myfile.name)

            print(uploaded_file_url)
            print("media/post_songs/" + myfile.name)

            audio = MP3("media/post_songs/" + myfile.name)
            # print(list(audio))
            # pics = None
            try:
                pics = audio.get('APIC:thumbnail').data
            except:
                pics = audio.get('APIC:').data

            # print(pics)
            img = Image.open(BytesIO(pics))
            img.save(f'media/post_songs/{myfile.name}.jpg')

            def property_by_tag_safe(tag_name):
                try:
                    return audio[tag_name]
                except:
                    return ""

            print(list(audio))
            # print(audio["TIT2"])  # Track
            # print(audio["TPE1"])  # Artist
            # print(audio['TALB'])  # Album
            # print(audio["TCON"])  # Genre
            # print(audio["TRCK"])  # TrackNumber 13/13
            # trackNumber = audio["TRCK"]
            # # print(audio["TPOS"])  # Disc
            # print(audio["TDRC"])  # Year
            # print(audio.info.length)  # Runtime
            # print(audio["USLT::XXX"])  # Lyrics

            playlist_name = audio["TALB"]

            playlists = Playlist.objects.filter(playlistName=playlist_name, artist=db_user)
            playlist = None
            if len(playlists) == 0:
                playlist = Playlist.objects.create(playlistName=playlist_name, artist=db_user)
            else:
                playlist = playlists[0]

            return Post.objects.create(user=user, song=file_addr, image=f'{file_addr}.jpg',
                                       title=property_by_tag_safe("TIT2"),
                                       runtime=audio.info.length, trackNumber=0,
                                       lyrics=property_by_tag_safe("USLT::XXX"),
                                       playlist=playlist)

        # add_song(request.FILES['file_0'])
        f = [add_song(x) for x in request.FILES.getlist('files')]
        print(f)

        return render(request, 'songs_edit.html', {'songs': f, 'user_profile': db_user})

    else:
        form = Post()
    return render(request, 'upload.html', {'form': form, 'user_profile': user_profile})


@login_required(login_url='signin')
def songs_edit(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    db_user = User.objects.get(username=request.user.username)

    print("here", request.POST["total"])

    if request.method == 'POST':
        print("hehehe:", request.POST["total"])
        for i in range(int(request.POST["total"])):
            post_id = request.POST[f'id_{i}']
            print(f"id: {post_id}")
            title = request.POST[f'title_{i}']
            print(f"title: {title}")
            print("---")

            p = Post.objects.get(id=post_id)

            genre_str = request.POST[f'genre_{i}']

            genre = Genre.objects.filter(name=genre_str)
            genre_obj = None
            if len(genre) == 0:
                genre_obj = Genre.objects.create(name=genre_str)
            else:
                genre_obj = genre[0]

            playlist_str = request.POST[f'playlist_{i}']
            playlist = Playlist.objects.filter(playlistName=playlist_str, artist=db_user)
            playlist_obj = None
            if len(playlist) == 0:
                playlist_obj = Playlist.objects.create(playlistName=playlist_str, artist=db_user)
            else:
                playlist_obj = playlist[0]

            p.title = title
            p.trackNumber = request.POST[f'track_number_{i}']
            p.caption = request.POST[f'caption_{i}']
            p.genre = genre_obj
            p.lyrics = request.POST[f'lyrics_{i}']
            # p.created_at = request.POST[f'created_at_{i}']
            print(request.POST[f'created_at_{i}'])
            p.isPublic = request.POST[f'is_public_{i}']
            p.playlist = playlist_obj

            p.save(update_fields=["title", "trackNumber", "caption", "genre", "lyrics", "isPublic", "playlist"])

        return redirect('success.html', {'songs': [], 'user_profile': db_user, 'user_profile': user_profile})
    else:
        form = Post()
    return render(request, 'songs_edit.html', {'songs': [], 'user_profile': db_user, 'user_profile': user_profile})


@login_required(login_url='signin')
def success(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    return render(request, 'success.html', {'user_profile': user_profile})


@login_required(login_url='signin')
def upload(request):
    if request.method == 'POST':

        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()

        return redirect('/')
    else:
        return redirect('/')


@login_required(login_url='signin')
def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':
        username = request.POST['username']
        username_object = User.objects.filter(username__icontains=username)

        username_profile = []
        username_profile_list = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_user=ids)
            username_profile_list.append(profile_lists)

        username_profile_list = list(chain(*username_profile_list))
    return render(request, 'search.html',
                  {'user_profile': user_profile, 'username_profile_list': username_profile_list})


@login_required(login_url='signin')
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes + 1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes - 1
        post.save()
        return redirect('/')


@login_required(login_url='signin')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)
    user_post_length = len(user_posts)

    follower = request.user.username
    user = pk

    if FollowersCount.objects.filter(follower=follower, user=user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'

    user_followers = len(FollowersCount.objects.filter(user=pk))
    user_following = len(FollowersCount.objects.filter(follower=pk))

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following,
    }
    return render(request, 'profile.html', context)


@login_required(login_url='signin')
def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if FollowersCount.objects.filter(follower=follower, user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('/profile/' + user)
        else:
            new_follower = FollowersCount.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/profile/' + user)
    else:
        return redirect('/')


@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':

        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

        return redirect('settings')
    return render(request, 'setting.html', {'user_profile': user_profile})


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                print("user: ", user, "username:", user.username)
                new_profile = Profile.objects.create(user=user, id_user=user.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, 'Password Is Not Matching')
            return redirect('signup')

    else:
        return render(request, 'registration/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'Username Or Password Is Invalid')
            return redirect('signin')

    else:
        return render(request, 'registration/signin.html')


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def about(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    return render(request, 'about.html', {'user_profile': user_profile})
