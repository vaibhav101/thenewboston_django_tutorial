from django.http import HttpResponse
from .models import Album
from django.shortcuts import render

def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums' : all_albums,
    }

    return render(request, 'music/index.html', context=context)


def detail(request, album_id):
    return HttpResponse("<h2> Details for album id: %d </h2>" % (album_id))
