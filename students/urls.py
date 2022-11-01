from django.urls import path
from students.views import students_index, student_details

urlpatterns= [
    path("index",students_index, name='students.index'),
    path("<int:student_id>",student_details, name='students.details')
]