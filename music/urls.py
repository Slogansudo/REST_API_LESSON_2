from django.urls import path, include
from .views import ArtistAPIView, ArtistDetailAPIView, AlbumDetailAPIView, AlbumAPIView, SongsAPIViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('songs', viewset=SongsAPIViewSet)

urlpatterns = [
    path('artists/', ArtistAPIView.as_view(), name='artists'),
    path('artists/<int:id>', ArtistDetailAPIView.as_view(), name='artist-detail'),
    path('albums/', AlbumAPIView.as_view(), name='albums'),
    path('albums/<int:id>', AlbumDetailAPIView.as_view(), name='album-detail'),
    path('', include(router.urls)),
]

