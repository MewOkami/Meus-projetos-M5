from django.urls import path
from . import views

# course_id = "uuid:pk"

urlpatterns = [
    path("courses/<uuid:course_id>/students/",
         views.StudentsCoursesView.as_view())
]
