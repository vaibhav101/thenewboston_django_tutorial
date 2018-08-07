from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello Buddy!!')


def detail(request, album_id):
    return HttpResponse("<h2> Details for album id: %d </h2>" % (album_id))
