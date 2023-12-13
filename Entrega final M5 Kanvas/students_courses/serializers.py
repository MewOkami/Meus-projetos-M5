from rest_framework import serializers
from .models import StudentCourse


class StudentsCoursesSerializer(serializers.ModelSerializer):
    student_id = serializers.CharField(read_only=True, source="student.id")
    student_username = serializers.CharField(
        read_only=True, source="student.username")
    student_email = serializers.CharField(
        source="student.email")

    class Meta:
        model = StudentCourse
        fields = [
            "id",
            "student_id",
            "student_username",
            "student_email",
            "status",
        ]
