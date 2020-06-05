from django.shortcuts import render
from adminEventRegistration.models import Announcements

def index(request):
    obj=Announcements.objects.latest('id')
    context={
        'obj':obj
    }
    return render(request,'homepage.html',context)