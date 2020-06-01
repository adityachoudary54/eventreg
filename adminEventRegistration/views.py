from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import userForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.conf import settings
from reg.models import Register
import adminEventRegistration.creatingPieChart as pie
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponse('Welcome to event registration')
    else:
        return HttpResponse("Unauthorized access")

def loginEventReg(request):
    form = userForm()
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('../display/')
            else:
                return HttpResponse("Unauthorized access")
    context = {"form": form}
    return render(request, "adminEventRegistration/login.html", context)

def display(request):
    if request.user.is_authenticated:
        querySet = Register.objects.all()
        pieChart= pie.createPie()
        context = {
            "objList": querySet,
            "pieChart":pieChart
        }
        return render(request, "adminEventRegistration/display.html", context)
    else:
        return HttpResponse("Unauthorized access")

def details(request,id):
    if request.user.is_authenticated:
        obj = Register.objects.get(id=id)
        context = {
            "obj": obj,
        }
        return render(request, "adminEventRegistration/details.html", context)
    else:
        return HttpResponse("Unauthorized access")