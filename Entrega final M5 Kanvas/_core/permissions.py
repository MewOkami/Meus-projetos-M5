from rest_framework import permissions
from rest_framework.views import Request, View
from accounts.models import Account
from students_courses.models import StudentCourse


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_superuser
        )


class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Account):
        if request.user.is_superuser:
            return True

        try:
            found_student = []
            found_course = []

            student_found = StudentCourse.objects.get(student=request.user.id)
            is_found = StudentCourse.objects.get(course=obj)

            found_student.append(student_found)
            found_course.append(is_found)
        except StudentCourse.DoesNotExist:
            return False

        if found_student == found_course:
            return True
        else:
            return False
