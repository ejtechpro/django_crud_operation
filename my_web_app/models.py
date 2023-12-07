from django.db import models

class Course(models.Model):
  course_title = models.CharField(max_length=100)
  
  def __str__(self):
    return self.course_title
  
  
class Student(models.Model):
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  first_name = models.CharField(max_length = 100)
  last_name = models.CharField(max_length=100)
  phone = models.IntegerField()
  gender = models.CharField(max_length=50)
  remarks = models.CharField(max_length=255)
  
 
 