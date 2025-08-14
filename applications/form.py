from django import forms
from .models import Attendance_Reports, Department, Employee, Duty_Duretion,Job_title,Leave


class AttendanceFrom(forms.ModelForm):
    class Meta:
        model = Attendance_Reports
        fields = "__all__"
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class EmployeeFrom(forms.ModelForm):
    class Meta:
        model = Employee 
        fields = ["fname", "lname", "gender", "age", "adderss", "email", "emp_password"]


class DepartmentFrom(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["dep_name"]


class Duty_DuretionForm(forms.ModelForm):
    class Meta:
        model = Duty_Duretion  
        fields = ["employee", "job", "duration"]


class Job_titleForm(forms.ModelForm): 
    class Meta:
        model = Job_title  
        fields = ["title", "dep_id"]


class LeaveForm(forms.ModelForm):  
    class Meta:
        model = Leave  
        fields = "__all__"