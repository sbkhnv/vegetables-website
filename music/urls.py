from django.urls import path,include
from .views import LandingPageAPIView,ArtistAPIView,AlbomDetailApiView,SongSetApiView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register("albom",viewset=AlbomDetailApiView)
router.register("songs",SongSetApiView)

urlpatterns = [
    path("artist/",ArtistAPIView.as_view(),name="artist"),
    path('',include(router.urls)),
    path("auth/",views.obtain_auth_token),
    # path("songs/<int:id>/",SongDetailApiView.as_view(),name="song-detail"),
    # path("songs/", SongsAPIView.as_view(), name="songs"),
]