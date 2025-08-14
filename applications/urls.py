from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('departments', DepartmentViewSet)
router.register('jobtitles', JobTitleViewSet)
router.register('employees', EmployeeViewSet)
router.register('dutyduration', DutyDurationViewSet)
router.register('leave', LeaveViewSet)
router.register('attendance', AttendanceReportsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
