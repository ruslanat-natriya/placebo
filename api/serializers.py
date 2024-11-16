from rest_framework import serializers
from .models import Employee, Position, Department


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'parent']


class EmployeeSerializer(serializers.ModelSerializer):
    current_position = serializers.PrimaryKeyRelatedField(queryset=Position.objects.all())
    available_positions = serializers.PrimaryKeyRelatedField(many=True, queryset=Position.objects.all())

    class Meta:
        model = Employee
        fields = ['id', 'name', 'current_position', 'available_positions']
