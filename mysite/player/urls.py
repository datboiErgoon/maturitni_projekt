from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main, name='main'),
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('upload_view', views.upload_view, name='upload_view'),
    path('songs_edit', views.songs_edit, name='songs_edit'),
    path('playlist_image_upload', views.playlist_image_upload, name='playlist_image_upload'),
    path('success', views.success, name='success'),
    path('play/<str:artist>/<str:album>/<str:song_id>', views.play, name='play'),
]
