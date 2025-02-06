from django.urls import path
from .views import MovieDetailView

urlpatterns = [
    path('api/v1/movie_app/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
]
