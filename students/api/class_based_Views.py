
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from students.api.serilizers import  StudentSerilalizer
from  students.models import Student


# class StudentAPIView(APIView):
#
#     def get(self, request):
#         students = Student.objects.all()
#         serialized_students = StudentSerilalizer(students, many=True)  # list of serialized object
#         print(serialized_students)
#         # return JsonResponse(serialized_students.data, safe=False, status=http.HTTPStatus.OK)
#         return Response(serialized_students.data, status=status.HTTP_200_OK)


#
# class StudentListView(ListAPIView):
#     serializer_class = StudentSerilalizer
#     queryset = Student.objects.all()
#     #
#     # def get_queryset(self):
#     #     pass


class StudentListView(ListCreateAPIView):
    serializer_class = StudentSerilalizer
    queryset = Student.objects.all()
    #
    # def get_queryset(self):
    #     pass

    # def create(self, request, *args, **kwargs):
    #     pass


class SingleStudnetView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerilalizer
    queryset = Student.objects.all()

    # def delete(self, request, *args, **kwargs):
    #     pass


"""
    GET, POST,  /StudentSet
     
     PUT, DELETE, GET   /StudentSet/<id>
"""
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerilalizer
    queryset = Student.objects.all()


