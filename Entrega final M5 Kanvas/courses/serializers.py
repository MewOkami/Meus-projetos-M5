from rest_framework import serializers
from contents.serializers import ContentSerializer
from students_courses.serializers import StudentsCoursesSerializer
from .models import Course
from accounts.models import Account


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]
        extra_kwargs = {
            "contents": {"read_only": True, "many": True},
            "students_courses": {"read_only": True, "many": True}
        }


class CourseDetailSerializer(serializers.ModelSerializer):
    students_courses = StudentsCoursesSerializer(
        many=True,
        read_only=True,
    )
    contents = ContentSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]


class StudentsDetailSerializer(serializers.ModelSerializer):
    students_courses = StudentsCoursesSerializer(
        many=True
    )

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "students_courses",
        ]
        extra_kwargs = {"id": {"read_only": True}, "name": {"read_only": True}}

    def update(self, instance, validated_data):
        students_Founds = []
        students_Not_Founds = []

        for studant_Course in validated_data["students_courses"]:
            print(studant_Course)
            studant = Account.objects.get(
                email=studant_Course["student"]["email"]
            )

            if not studant:
                students_Not_Founds.append(studant_Course["student"]["email"])
            else:
                students_Founds.append(studant)

            if students_Not_Founds:
                raise serializers.ValidationError({
                    "detail": f"No active accounts was found: {', '.join(students_Not_Founds)}."
                })

            instance.students.add(*students_Founds)
        return instance
