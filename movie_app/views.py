from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie  # Импортируем правильную модель
from .serializers import MovieSerializer  # Импортируем правильный сериализатор

class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()  # Исправлено: заменили Product на Movie
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        try:
            movie = self.get_object()
            serializer = self.get_serializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
