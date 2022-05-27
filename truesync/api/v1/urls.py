from django.urls import path
from .auth.views import login_view, registration_view, ProfileView
from .courses.views import CourseListView, CourseDetailView, CourseDetailSlugView


urlpatterns = [
    path('auth/login/', login_view),
    path('auth/register/', registration_view),
    path('auth/profile/', ProfileView.as_view()),
    
    path('courses/', CourseListView.as_view()),
    path('courses/<uuid:pk>/', CourseDetailView.as_view()),
    path('courses/<slug:course_slug>/slug/', CourseDetailSlugView.as_view()),
]