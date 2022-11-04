from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from .serializer import SongSerializer
from .serializer import LyricSerializer
from musicapp.models import Song, Lyric

#from django_project.songcrud.musicapp import serializer


# Create your views here.
#def index(request):
    #return HttpResponse("My first django musicapp")

@csrf_exempt
def song_list_api(request):
    if request.method == "GET":
        songcrud= Song.objects.all()
        serializer = SongSerializer (songcrud, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SongSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def song_detail_api (request, id):
    try:
        song = Song.objects.get(id=id)
    except Song.DoesNotExist:
        return JsonResponse({"message": "Song not found"}, status=404)

    if request.method == "GET":
        serializer = SongSerializer(song)
        return JsonResponse(serializer.data, status=200)
    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer =SongSerializer(song, data=data)
        if serializer. is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors,status=400)   
    if request.method == "DELETE": 
        song.delete()
        return JsonResponse({"message: Song deleted"}, status=204)


@csrf_exempt
def lyric_list_api(request):
    if request.method == "GET":
        songcrud= Lyric.objects.all()
        serializer = LyricSerializer (songcrud, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = LyricSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def lyric_detail_api (request, id):
    try:
        lyric = Lyric.objects.get(id=id)
    except Lyric.DoesNotExist:
        return JsonResponse({"message": "Lyric not found"}, status=404)

    if request.method == "GET":
        serializer = LyricSerializer(lyric)
        return JsonResponse(serializer.data, status=200)
    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer =LyricSerializer(lyric, data=data)
        if serializer. is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors,status=400)   
    if request.method == "DELETE": 
        lyric.delete()
        return JsonResponse({"message: Lyric deleted"}, status=204)

