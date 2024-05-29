from ctypes import addressof
from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField(primary_key=True)
    address=models.TextField()
    farther_name=models.CharField(default="Rahim",max_length=20)
    
    def __str__(self) -> str:
        return f"Roll : {self.roll} Name : {self.name}"

class StudentModel(models.Model):
    roll =models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    father_name=models.CharField(max_length=30)
    address=models.TextField()