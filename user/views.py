from functools import partial
from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user import serializers

from user.models import Student
from user.serializers import StudentSerializer

# Create your views here.

@api_view(['GET'])
def index(request):

    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response({'status': 200, 'payload': serializer.data})


@api_view(['POST'])
def createuser(request):
    data = request.data
    serializer = StudentSerializer(data=data)
    if not serializer.is_valid():
        return Response({'status': 403, 'message': 'something went wrong'})
    serializer.save()
    return Response({'status': 200, 'payload': 'your data has been saved..'})


@api_view(['PATCH'])
def change(request, id):
    id = int(id)
    try:
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'status': 403, 'message': 'You typed wrong data formate'})

        serializer.save()
        return Response({'status': 200, 'payload': 'your data has been Updated..'})
    
    except Exception as e:
        return Response({'status': 403, 'message': 'invalid id'})

@api_view(["DELETE"])
def delete(request, id):
    id = int(id)
    try:
        student = Student.objects.get(id=id)
        student.delete()
        return Response({'status': 200, 'payload': 'user now deleted'})
    except Exception as e:
        return Response({'status': 403, 'payload': 'invalid id'})