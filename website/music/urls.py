from django.urls import path
from . import views


urlpatterns = [
    # ex: /music/
    path('', views.index, name='index'),
    # ex: /music/71/
    path('<int:album_id>/', views.detail, name='detail'),
]