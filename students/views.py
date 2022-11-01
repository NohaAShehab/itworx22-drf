import http
import json

from django.shortcuts import render, get_object_or_404, reverse
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from students.models import Student, Track

@csrf_exempt
def students_index(request):
    if request.method == "GET":
        students = Student.objects.all()
        serialized_students = []
        for student in students:
            serialized_students.append(serialize_student(student))
        return JsonResponse(serialized_students, safe=False, status=http.HTTPStatus.OK)
    elif request.method=="POST":
        ## accept data sent to the application
        print(request.body)
        ## create new object
        body = json.loads(request.body)  # dictioonary
        print(body, type(body))

        ## save object
        """ Student.objects.create(name='noha', email='nnn')"""
        student =Student.objects.create(**body)  #### Student Model object
        ### return the save object
        # return JsonResponse("Hi, I am the post method", safe=False)
        return JsonResponse(serialize_student(student), safe=False, status=http.HTTPStatus.CREATED)

@csrf_exempt
def student_details(request, student_id):
    if request.method =="GET":
        student = get_object_or_404(Student, pk=student_id)
        return JsonResponse(serialize_student(student), status=http.HTTPStatus.OK)
    elif request.method=="PUT":
        student = get_object_or_404(Student, pk=student_id)
        body = json.loads(request.body)  # dictioonary
        student.name = body["name"]
        try:
            student.track = Track.objects.get(id=body["track_id"])
        except:
            pass
        student.age = body["age"]
        student.salary = body["salary"]
        student.save()
        return JsonResponse(serialize_student(student), status=http.HTTPStatus.OK)


    elif request.method =="DELETE":
        try:
            student = Student.objects.get(id=student_id)
            if student:
                student.delete()
                return JsonResponse({"deleted":1}, status=http.HTTPStatus.NO_CONTENT)
        except:
                return JsonResponse({"deleted": 0}, status=http.HTTPStatus.RESET_CONTENT)



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