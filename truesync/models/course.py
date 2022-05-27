from django.db import models
from django.contrib.postgres.fields import ArrayField
from . base import BaseUUIDModel
from . category import Category


class Course(BaseUUIDModel):
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='category_courses',
        db_index=True
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    objectives = ArrayField(models.TextField(), blank=True, null=True)
    requirements = ArrayField(models.TextField(), blank=True, null=True)
    thumbnail = models.CharField(max_length=200, blank=True, null=True)
    preview = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'courses'

    def __str__(self) -> str:
        return self.title

    def thumbnail_url(self):
        return 's3/' + self.thumbnail