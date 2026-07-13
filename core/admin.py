from django.contrib import admin
from .models import Department, Student, Course, Enrollment


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "age",
        "department",
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
    )
    list_filter = ("department",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "code",
        "department",
    )
    search_fields = ("name", "code")
    list_filter = ("department",)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "student",
        "course",
        "enrolled_at",
    )
    list_filter = (
        "course",
        "enrolled_at",
    )