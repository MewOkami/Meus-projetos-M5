from courses.models import Course
from .models import Content
from .serializers import ContentSerializer
from rest_framework.exceptions import NotFound
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from _core.permissions import IsAdminOrReadOnly, IsUserOwner
from rest_framework.permissions import IsAuthenticated


class ContentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        course = Course.objects.filter(pk=self.kwargs["course_id"]).first()
        if not course:
            raise NotFound({"detail": "Not found."})
        serializer.save(course=course)


class ContentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserOwner]

    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_field = 'pk'
