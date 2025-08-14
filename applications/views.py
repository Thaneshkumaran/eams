from django.shortcuts import render,HttpResponse
from .form import *
from .models import *
from django.http import JsonResponse
# Create your views here.

def form(request):
    data={
        "form" : AttendanceFrom(),
        "name": "Attendance From",
        "url" : "create_Attendance/"
    }
    return render(request,"./form.html",{"data":data})

def home(request):
    return HttpResponse("helle thanesh")
def create_Attendance(request):
    if request== "POST":
        pass
    return JsonResponse({"success": True, "redirect_url": "/home"})
