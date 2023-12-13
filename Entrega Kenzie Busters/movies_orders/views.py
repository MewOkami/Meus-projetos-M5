from rest_framework.views import APIView, status, Request, Response
# from .models import MovieOrder
from movies.models import Movie
from .serializers import MovieOrderSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id: int) -> Response:
        found_movie = get_object_or_404(Movie, pk=movie_id)
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(
            movie=found_movie,
            user=request.user,
            title=found_movie.title,
            purchased_by=request.user.email
        )

        return Response(serializer.data, status.HTTP_201_CREATED)
