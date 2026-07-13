from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Department, Student, Course, Enrollment

from .serializers import (
    DepartmentSerializer,
    StudentSerializer,
    CourseSerializer,
    EnrollmentSerializer,
)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    search_fields = [
        "first_name",
        "last_name",
        "email",
    ]

    filterset_fields = [
        "department",
        "age",
    ]

    ordering_fields = [
        "age",
        "first_name",
        "last_name",
    ]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

def home(request):
    return HttpResponse("Welcome to Student Management API")