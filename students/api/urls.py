from django.urls import path, include
from students.api.views import student_api

urlpatterns= [
    path("", student_api, name="student.api")
]