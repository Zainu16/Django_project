from django.urls import path
from .views import song_list_api, song_detail_api


from . import views
urlpatterns = [
    #path("", views.index, name="index"),
    path("songcrud/", song_list_api, name="song_list_api"),
    path("songcrud/<int:id>/", song_detail_api, name="song_detail_api"),
]    