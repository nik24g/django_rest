from rest_framework import serializers

from user.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['id', 'name', 'address']
        fields = '__all__'
        # exclude = ['rollno']
