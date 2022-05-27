from rest_framework import generics, exceptions

from truesync.models.course import Course
from . serializers import CourseListSerializer, CourseDetailSerializer


class CourseNotFoundException(exceptions.APIException):
    status_code = 404
    default_detail = 'Course not found'
    default_code = 'course_not_found'


class CourseListView(generics.ListAPIView):
    serializer_class = CourseListSerializer
    queryset = Course.objects.all()


class CourseDetailView(generics.RetrieveAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()


class CourseDetailSlugView(generics.RetrieveAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()

    def get_object(self):
        course_slug = self.kwargs.get('course_slug')
        try:
            course = Course.objects.get(slug=course_slug)
        except Course.DoesNotExist:
            raise CourseNotFoundException
        return course