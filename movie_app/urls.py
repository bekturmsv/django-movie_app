from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import DirectorsViewSet, MoviesViewSet, ReviewsViewSet




urlpatterns = [
    # path('movies/', MovieList.as_view(), name='movie-list'),
    # path('movies/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
    # path('movies/reviews/', MovieReviewsList.as_view(), name='movie-reviews-list'),
    # path('reviews/', ReviewList.as_view(), name='review-list'),
    # path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('directors/', DirectorsViewSet.as_view({'get': 'list'}) , name="director"),
    path('reviews/', ReviewsViewSet.as_view({'get': 'list', 'post': 'create'}) , name="review"),
    path('movies/', MoviesViewSet.as_view({'get': 'list', 'post': 'create'}) , name="movie")
]
