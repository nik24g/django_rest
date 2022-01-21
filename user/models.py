from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    rollno = models.IntegerField()
    mobile = models.IntegerField()
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name
