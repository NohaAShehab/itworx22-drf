import http

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from students.models import Student
from students.api.serilizers import StudentSerilalizer


@api_view(["GET", "POST"])
def student_api(request):
    if request.method == "GET":
        students = Student.objects.all()
        serialized_students = StudentSerilalizer(students, many=True)  # list of serialized object
        print(serialized_students)
        # return JsonResponse(serialized_students.data, safe=False, status=http.HTTPStatus.OK)
        return Response(serialized_students.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        # data = request.body
        # print(request.body, request.data)
        # request.data is dictionary
        student = StudentSerilalizer(data=request.data)
        if student.is_valid():
            student.save()
            return Response(student.data, status=status.HTTP_201_CREATED)

        return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)
