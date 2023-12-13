from rest_framework.views import APIView, status, Request, Response
from .models import Movie
from .serializers import MovieSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, req: Request) -> Response:
        movies = Movie.objects.all()
        result = self.paginate_queryset(movies, req)
        serializer = MovieSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)


class MovietDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, req: Request, movie_id: int) -> Response:
        try:
            found_movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response(
                {"detail": "Not found."},
                status.HTTP_404_NOT_FOUND,
            )

        serializer = MovieSerializer(found_movie)
        return Response(serializer.data)

    def delete(self, req: Request, movie_id: int) -> Response:
        try:
            found_movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response(
                {"detail": "Not found."},
                status.HTTP_404_NOT_FOUND,
            )

        found_movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
