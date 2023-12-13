from django.urls import path
from . import views

course_id = "str:course_id"
content_id = "str:pk"

urlpatterns = [
    path(f'courses/<{course_id}>/contents/', views.ContentView.as_view()),
    path(f'courses/<{course_id}>/contents/<{content_id}>/',
         views.ContentDetailView.as_view())
]
