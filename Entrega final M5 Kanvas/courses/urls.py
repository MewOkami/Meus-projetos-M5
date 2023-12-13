from django.urls import path
from . import views

course_id = "str:pk"

urlpatterns = [
    path("courses/", views.CourseView.as_view()),
    path(f'courses/<{course_id}>/', views.CourseDetailView.as_view())
]
