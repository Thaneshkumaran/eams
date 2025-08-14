from .models import *
from django.contrib import admin

models_to_register = [Attendance_Reports,Department,Employee,Duty_Duretion,Job_title,Leave,Gender]
admin.site.register(models_to_register)
# for model in models_to_register:
#     admin.site.register(model)
