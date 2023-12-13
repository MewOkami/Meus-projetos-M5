from .models import Course
from .serializers import CourseSerializer
from .serializers import CourseDetailSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from _core.permissions import IsAdminOrReadOnly, IsUserOwner
from rest_framework.permissions import IsAuthenticated


class CourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserOwner]

    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    lookup_field = 'pk'
