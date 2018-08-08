from .models import Album, Song
from django.shortcuts import render, get_object_or_404


def index(request):
    all_albums = Album.objects.all()

    context = {
        'all_albums': all_albums,
    }

    return render(request, 'music/index.html', context=context)


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    context = {
        'album': album,
    }

    return render(request, 'music/detail.html', context=context)


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    context = {
        'album': album,
    }

    try:
        selected_song = album.song_set.get(pk = request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        context['error_message'] = "You did not select a valid song!"
        return render(request, 'music/detail.html', context=context)
    else:
        context['error_message'] = "Favorite set!"
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', context=context)
