from rest_framework import serializers
from .models import Department, JobTitle, Employee, DutyDuration, Leave, AttendanceReports

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DutyDurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DutyDuration
        fields = '__all__'

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = '__all__'

class AttendanceReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceReports
        fields = '__all__'
