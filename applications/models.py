from django.db import models


class Department(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class JobTitle(models.Model):
    job_title = models.CharField(max_length=100)
    dept_ID = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_title


class Gender(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    age = models.IntegerField()
    contact_add = models.TextField()
    emp_email = models.EmailField(unique=True)
    emp_pass = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fname} {self.lname}"


class DutyDuration(models.Model):
    employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job_ID = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    duration = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"Duty {self.id} - {self.employee_ID}"   # use self.id


class Leave(models.Model):
    employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job_ID = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"Leave {self.id} - {self.employee_ID}"   # use self.id


class AttendanceReports(models.Model):
    employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    duty_ID = models.ForeignKey(DutyDuration, on_delete=models.CASCADE)
    job_ID = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    leave_ID = models.ForeignKey(Leave, on_delete=models.CASCADE)
    total_labor = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"Report {self.id} - {self.employee_ID}"   # use self.id
