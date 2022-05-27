from rest_framework import serializers
from truesync.models import Course


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'slug',
            'created_at'
        ]


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'slug',
            'description',
            'price',
            'objectives',
            'requirements',
            'thumbnail_url',
            'created_at',
            'updated_at'
        ]