from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import uuid as u
from datetime import datetime
from .models import Register
# Create your views here.
def formfields():
    f=['username','mobile','email','idcard','regType','noTickets']
    return f

def index(request):
    
    rs=request.session
    rs['previous']=rs.get('previous',False)
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
        request.session['confirm']=False
        # rs['previous']=False
        return redirect('register:temp')
    
    
    return render(request,'reg/userForm.html',)
    

def tempView(request):
    
    if request.method=='POST':
        rs=request.session
        
        
        if(request.POST.get('confirm')=='1' and rs['confirm']==False):
            i=u.uuid4()
            t=i.hex
            user=Register(regId=i.hex, username=rs['username'], mobile=rs['mobile'], email=rs['email'], regType=rs['regType'], noTickets=rs['noTickets'])
            user.idcard=rs['idcard'].replace('/media','')
            rs['confirm']=True
            user.save()
            context={}
            for i in formfields():
                context[i]=request.session[i]
            context['regid']=str(t)
            return render(request,'reg/successForm.html',context=context)
        else:
            
            return redirect('register:index')
    context={}
    for i in formfields()+['idcard']:
        context[i]=request.session[i]
    print(context)
    return render(request,'reg/previewForm.html',context)
    