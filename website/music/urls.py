from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # ex: /music/
    path('', views.index, name='index'),
    # ex: /music/71/
    path('<int:album_id>/', views.detail, name='detail'),
    # ex: /music/71/favorite
    path('<int:album_id>/favorite/', views.favorite, name='favorite'),
]
