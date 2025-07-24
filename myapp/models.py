from django.contrib.auth.models import User
from django.db import models
from common.models import GradeChoice


class Subject(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    grade = models.CharField(max_length=100, choices=GradeChoice, null=True, blank=True)
    credit = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} - {self.grade}, credit {self.credit}'


