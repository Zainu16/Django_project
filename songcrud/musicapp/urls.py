from django.urls import path
from .views import song_list_api, song_detail_api
from .views import lyric_list_api,lyric_detail_api


from . import views
urlpatterns = [
    #path("", views.index, name="index"),
    path("songcrud/", song_list_api, name="song_list_api"),
    path("songcrud/<int:id>/", song_detail_api, name="song_detail_api"),
    path("songcrud/", lyric_list_api, name="lyric_list_api"),
    path("songcrud/<int:id>/", lyric_detail_api, name="lyric_detail_api"),
]    