from rest_framework.views import APIView, status, Request, Response
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .models import User
from movies.permissions import IsUserOwner
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class UserView(APIView):
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UsertDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserOwner]

    def get(self, req: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(req, found_user)

        serializer = UserSerializer(found_user)
        return Response(serializer.data)

    def patch(self, req: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(req, found_user)
        serializer = UserSerializer(found_user, data=req.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data)
