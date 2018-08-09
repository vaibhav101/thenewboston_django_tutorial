from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # ex: /music/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /music/71/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
]
