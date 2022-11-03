from django.urls import path, include
from students.views import students_index, student_details

urlpatterns= [
    path("index",students_index, name='students.index'),
    path("<int:student_id>",student_details, name='students.details'),
    path("api/", include("students.api.urls")),

]