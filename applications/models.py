from django.db import models

# Create your models here.
class Gender(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Department(models.Model):
    dep_id = models.AutoField(primary_key=True)
    dep_name = models.CharField(max_length=120)

    def __str__(self):
        return self.dep_name


class Job_title(models.Model):
    Job_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    dep_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=120)
    lname = models.CharField(max_length=120)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    age = models.IntegerField()
    adderss = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    emp_password = models.CharField(max_length=128) 

    def __str__(self):
        return self.fname


class Leave(models.Model):
    Leave_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job_title, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.employee)
class Duty_Duretion(models.Model):
    Duty_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job_title, on_delete=models.CASCADE)
    duration = models.DurationField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.employee)


class Attendance_Reports(models.Model):
    report_id = models.AutoField(primary_key=True)
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    duty_id = models.ForeignKey(Duty_Duretion, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job_title, on_delete=models.CASCADE)
    Leave_id = models.ForeignKey(Leave, on_delete=models.CASCADE)
    total_laber = models.CharField(max_length=120)
    salary = models.IntegerField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.report_id)
