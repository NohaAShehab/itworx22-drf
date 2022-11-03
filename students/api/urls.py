from django.urls import path, include
from students.api.views import student_api, student_operations
from students.api.class_based_Views import StudentListView, SingleStudnetView, StudentViewSet


urlpatterns= [
    path("/m", student_api, name="student.api"),
    path("<int:id>",student_operations, name="students.operations" ),
    path("class", StudentListView.as_view(), name="students.class"),
    path("class/<int:pk>", SingleStudnetView.as_view(), name="students.singleclass"),

]