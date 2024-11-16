from django.contrib import admin
from .models import Position, Department, Employee


class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('permissions',)  # Позволяет выбирать права для должностей


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('parent',)
    filter_horizontal = ('positions',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'current_position')
    filter_horizontal = ('available_positions',)


admin.site.register(Position, PositionAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
