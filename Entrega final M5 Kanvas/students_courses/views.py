from courses.models import Course
from courses.serializers import StudentsDetailSerializer
from rest_framework.generics import (
    RetrieveUpdateAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from _core.permissions import IsAdminOrReadOnly


class StudentsCoursesView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Course.objects.all()
    serializer_class = StudentsDetailSerializer
    lookup_url_kwarg = 'course_id'
