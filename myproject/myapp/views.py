from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Course
from .form import CourseForm


def course_list(request):
    courses = Course.objects.all()
    form = CourseForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('course_list')
    return render(request, 'courses.html', {'courses': courses, 'form': form})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .form import CourseForm

# Create + List
def course_list(request):
    courses = Course.objects.all()
    form = CourseForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('courses')
    return render(request, 'courses.html', {'courses': courses, 'form': form})

# Read (Detail View)
def courseDetail(request, id):
    course_detail = get_object_or_404(Course, id=id)
    return render(request, 'coursedetail.html', {'course_detail': course_detail})

# Create (Separate Page)
def course_create(request):
    form = CourseForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('courses')
    return render(request, 'course_create.html', {'form': form})

# Update
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, request.FILES or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('courses')
    return render(request, 'course_form.html', {'form': form})

# Delete
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('courses')
    return render(request, 'course_confirm_delete.html', {'course': course})

def homepage(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def event(request):
    return render(request, 'events.html')

def trainer(request):
    return render(request, 'trainers.html')
