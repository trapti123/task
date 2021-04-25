from django.shortcuts import render
from rest_framework.response import Response# return response
from rest_framework.decorators import api_view#for method
from .serializer import StudentSerializer
from .models import Student
# Create your views here.



@api_view(['GET'])
def listStudent(request):
    
    student = Student.objects.all()
    serializer = StudentSerializer(student,many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addStudent(request):
    serializer = StudentSerializer(data = request.data)

    if serializer.is_valid():#check the data
        serializer.save()
        return Response(serializer.data)
    
    
