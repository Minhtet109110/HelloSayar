from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('course/', course_list, name='courses'),  # List + Create in one page
    path('event/', event, name='event'),
    path('trainer/', trainer, name='trainer'),

    # CRUD Routes
    path('coursesDetail/<int:id>/', courseDetail, name='courseDetail'),     # Read (Detail View)
    path('courses/create/', course_create, name='course_create'),           # Create
    path('courses/update/<int:pk>/', course_update, name='course_update'),  # Update
    path('courses/delete/<int:pk>/', course_delete, name='course_delete'),  # Delete
]