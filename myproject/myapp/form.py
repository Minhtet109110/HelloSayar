from django import forms
from myapp.models import Course,Teacher


    

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields =['photo', 'name', 'fee', 'description']

class TeacherModelForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['photo', 'name', 'fee', 'description']