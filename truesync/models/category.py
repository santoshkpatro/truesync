from django.db import models
from . base import BaseUUIDModel


class Category(BaseUUIDModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        db_table = 'categories'

    def __str__(self) -> str:
        return self.name