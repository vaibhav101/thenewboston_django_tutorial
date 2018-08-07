from django.http import Http404
from .models import Album
from django.shortcuts import render


def index(request):
    all_albums = Album.objects.all()

    context = {
        'all_albums' : all_albums,
    }

    return render(request, 'music/index.html', context=context)


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist!")

    context = {
        'album' : album,
    }

    return render(request, 'music/detail.html', context=context)