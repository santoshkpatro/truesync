from django.db import models
from . base import BaseUUIDModel
from . course import Course
from . user import User


class Enrollment(BaseUUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_enrollments')
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        db_table = 'enrollments'

    def __str__(self) -> str:
        return str(self.id)