from rest_framework import serializers
from .models import *

class Attendance_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance_Reports
        fields = ["__all__"]
class Attendance_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance_Reports
        fields = ["__all__"]