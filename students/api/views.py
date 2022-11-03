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


#### Show , edit , delete

def get_student_object_or_none(model, id):
    try:
        student = model.objects.get(pk=id)
    except:
        return None

    return student





@api_view(["GET", "PUT", "DELETE"])
def student_operations(request, id):
    student = get_student_object_or_none(Student, id)
    if request.method == "GET":
        if student:
            serialized_student = StudentSerilalizer(student)
            return Response(serialized_student.data, status=status.HTTP_200_OK)
        return Response({"found":0}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == "PUT":
        if student:
            serialized_student = StudentSerilalizer(student, data=request.data)
            if serialized_student.is_valid():
                serialized_student.save()
                return Response(serialized_student.data, status=status.HTTP_200_OK)
            else:
                return Response(serialized_student.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"found":1}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        if student:
            student.delete()
            return Response({"deleted":1}, status=status.HTTP_204_NO_CONTENT)
        return Response({"found": 0}, status=status.HTTP_205_RESET_CONTENT)
