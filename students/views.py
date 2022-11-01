from django.shortcuts import render, get_object_or_404, reverse
from django.http import JsonResponse, HttpResponse

# Create your views here.
from students.models import Student, Track


def students_index(request):
    if request.method == "GET":
        students = Student.objects.all()
        serialized_students = []

        for student in students:
            # serialized_students.append({
            #         "id":student.id,
            #         "name":student.name,
            #         "age":student.age,
            #         "salary": student.salary,
            #         "track":{
            #             "id": student.track.id if student.track else None,
            #             "name": student.track.name if student.track else None
            #         },
            #         "created_at": student.created_at,
            #         "updated_at": student.updated_at
            # })
            serialized_students.append(serialize_student(student))

        return JsonResponse(serialized_students, safe=False)
        # for student in students:
        #     serialized_students.append({
        #             "id":student.id,
        #             "name":student.name,
        #             "track":student.track.id,
        #             "list": [2,4,5]
        #     })
        #
        # ss = {"students":serialized_students}
        #
        # return JsonResponse(ss)


def student_details(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return JsonResponse(serialize_student(student))


def serialize_student(student):
    return {
        "href": reverse("students.details", args=[student.id]),
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "salary": student.salary,
        "track": {
            "id": student.track.id if student.track else None,
            "name": student.track.name if student.track else None
        },
        "created_at": student.created_at,
        "updated_at": student.updated_at
    }



"""
    actions ----> 
    Request Methods 
    GET all objects ---> Status code 200
    GET Specific object ---> Status code 200
    POST new object ----> Status code 201
    Put/Patch existing object ---> Status code 200
    DELETE existing object ---> Status code 204 (object has been removed)
                                            205 (You need to reset this content)
    




"""