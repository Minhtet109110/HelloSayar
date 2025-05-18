from django.db import models

# Create your models here.
class Course(models.Model):
    photo =models.ImageField(upload_to='course')
    name =models.CharField(max_length=255)
    fee =models.PositiveBigIntegerField(default=0)
    description = models.TextField(max_length=255)


class Teacher(models.Model):
    photo =models.ImageField(upload_to='teacher')
    name = models.CharField(max_length=255)
    course = models.TextField(max_length=255) 
    fee =models.PositiveBigIntegerField(default=0)
    description = models.TextField(max_length=255)

