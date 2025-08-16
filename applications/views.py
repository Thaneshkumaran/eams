from rest_framework import viewsets
from .models import Department, Gender, JobTitle, Employee, DutyDuration, Leave, AttendanceReports
from .serializers import *
from django.shortcuts import render

def index(request):
    return render(request,"index.html")
class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class JobTitleViewSet(viewsets.ModelViewSet):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DutyDurationViewSet(viewsets.ModelViewSet):
    queryset = DutyDuration.objects.all()
    serializer_class = DutyDurationSerializer

class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer

class AttendanceReportsViewSet(viewsets.ModelViewSet):
    queryset = AttendanceReports.objects.all()
    serializer_class = AttendanceReportsSerializer
