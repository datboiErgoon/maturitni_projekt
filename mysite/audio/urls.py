from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('player/', views.SongListView.as_view(), name='song_list'),
    path('player/<int:pk>', views.SongDetailView.as_view(), name='song_detail'),
    path('player/create', views.SongCreate.as_view(), name='song_create')
]