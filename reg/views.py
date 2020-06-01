from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import uuid as u
from datetime import datetime
from .models import Register

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.conf import settings
# Create your views here.
def formfields():
    f=['username','mobile','email','idcard','regType','noTickets']
    return f

def index(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            rs=request.session
            getpost=request.POST.get
            
            for i in formfields():
                rs[i]=getpost(i)    
            
            # File storage
            myfile=request.FILES['idcard']
            fs=FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            # 
            request.session['idcard']=uploaded_file_url

            # for i in formfields()+['idcard']:
            #     print(request.session[i])

            return redirect('temp')
        
        return render(request,'reg/userForm.html')
    else:
        return HttpResponse("Unauthorized access")


def tempView(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            rs=request.session
        
            print('Submit FIle')
            if(request.POST.get('confirm')=='1'):
                i=u.uuid4()
                user=Register(regId=i.hex, username=rs['username'], mobile=rs['mobile'], email=rs['email'], regType=rs['regType'], noTickets=rs['noTickets'])
                user.idcard=rs['idcard'].replace('/media','')
                user.save()

                return HttpResponse(f'Successful Submission. ID is: {i.hex} len:{len(i.hex)}')
            else:
                return redirect('index')
        rs=request.session
        context={}
        for i in formfields()+['idcard']:
            context[i]=request.session[i]
        print(context)
        return render(request,'reg/previewForm.html',context)
    else:
        return HttpResponse("Unauthorized access")