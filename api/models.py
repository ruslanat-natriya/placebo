from django.db import models
from django.contrib.auth.models import Permission


class Department(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subdepartments')
    positions = models.ManyToManyField('Position', related_name='departments', blank=True)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.ManyToManyField(Permission, related_name='positions', blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    current_position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, related_name='current_employees')
    available_positions = models.ManyToManyField(Position, blank=True, related_name='available_employees')

    def __str__(self):
        return self.name
