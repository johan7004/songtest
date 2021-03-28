from django.urls import path
from .views import home ,lyricsview

urlpatterns = [
    path('', home, name='home'),
    path('<slug:slug>/', lyricsview.as_view(),name='lyric-detail')
]
