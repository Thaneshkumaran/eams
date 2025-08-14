from .models import *
from django.contrib import admin

models_to_register = [Department, JobTitle, Employee, DutyDuration, Leave, AttendanceReports,Gender]
admin.site.register(models_to_register)
# for model in models_to_register:
#     admin.site.register(model)
