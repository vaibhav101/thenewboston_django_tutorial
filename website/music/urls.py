from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # ex: /music/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /music/register
    path('register/', views.UserFormView.as_view(), name='register'),
    # ex: /music/71/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
    # ex: /music/album/71/
    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),
    # ex: /music/album/71/delete
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),
]
