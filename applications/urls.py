
from django.urls import path
from . import views

urlpatterns = [
    path('',views.form,name="index"),
    path("home",views.home,name="home"),
    path('create_Attendance/',views.create_Attendance,name="create_Attendance"),
]

