from django.shortcuts import render ,redirect
from .models import AdminDataBase ,Customer
from django.shortcuts import render,HttpResponseRedirect
from  django.http import HttpResponse

def home(req):
    return render(req,'app/home.html')
def about(req):
    return render(req,'app/about.html')
def schedule(req):
    return render(req,'app/schedule.html')


#=============================ADMIN=======================================
def adminlogin(req):
    return render(req,'app/adminlogin.html')


def AdminRegistration(request):
    return render(request,"app/AdminRegistration.html")

#=====================admin login===========================================================================
from django.shortcuts import render, redirect
from django.contrib import messages

def adminloginpage_fetch(request):
    if request.method == 'POST':
        a = request.POST.get('email')
        p = request.POST.get('password')
        
        try:
            user = AdminDataBase.objects.get(Email=a)
            
            if user.Password == p:
                mydata = AdminDataBase.objects.filter(Email=a).values()
                return render(request, 'app/adminDashboard.html', {'msg': mydata})
            else:
                messages.error(request, 'Password is incorrect')
        except AdminDataBase.DoesNotExist:
            messages.error(request, 'Email is incorrect  type  correct email')
    
    return render(request, 'app/adminlogin.html')

# def adminloginpage_fetch(request):
#     if request.method=='POST':
#         # print(request.POST)
       
#         a=request.POST['email']
#         p=request.POST['password']
#         user=AdminDataBase.objects.get(Email=a)
#         # print(user.values())
#         # print(user.fname)
#         if user:
#             if user.Password==p:
#                 mydata = AdminDataBase.objects.filter(Email=a).values()
#                 print(mydata)
#                 return render(request,'app/adminDashboard.html',{'msg':mydata})
#         else:
#             msg="First Name not matched"
#             return render(request,'app/adminlogin.html',{'msg':msg})
#     else:
#         msg="user dose not exit please register first"
#         return render(request,'app/adminlogin.html',{'msg':msg})
#=====================admin login end================================================ 
#=======================ADMIN REGISTRATION================================================================
def aregistration(request):
     if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        user = AdminDataBase.objects.filter(Email=email)
        if user:
            msg= "User already exist please login"
            return render(request,'app/AdminRegistration.html',{'msg':msg})
        else:
            if password==cpassword:
                newdatainsert = AdminDataBase.objects.create(FirstName=fname,lastName=lname,Email=email,Contact=contact,Password=password)
                msg = "User register Successfully go to admin login page"
                return render(request,'app/AdminRegistration.html',{'msg':msg})
            else:
                msg="Password and Confirm Password not match!"
                return render(request, 'app/AdminRegistration.html',{'msg':msg})
     return render(request,'app/AdminRegistration.html')
 #=======================ADMIN REGISTRATION end=====================================================================

def adminDashboard(request):
     return render(request,'app/adminDashboard.html')
 
 
 
 
 
 
 
 
 
 
 


def form(request):
    if request.method=="POST":
        print(request.POST)
        a=request.POST.get('fname')
        b=request.POST.get('lname')
        c=request.POST.get('email')
        d=request.POST.get('age')
        idd=request.POST.get('identity')
        e=request.FILES.get('image')
        instance=Customer(name=a , lname=b , email=c , age=d , identity=idd ,image=e)
        instance.save()
        msg="register successfull go to show all record"      
    return render(request,"app/adminDashboard.html",{'a':msg})




def allrecord(request):
    d=Customer.objects.all() #quearyset
    print(d)
    return render(request,"app/allrecord.html",{'data':d }) 



def update(request,id):
    if request.method=="POST":
        a=request.POST.get('fname')
        b=request.POST.get('lname')
        c=request.POST.get('email')
        d=request.POST.get('age')
        idd=request.POST.get('identity')
        e=request.FILES.get('image')
        if e==None:
            Customer.objects.filter(id=id).update(name=a ,lname=b , email=c ,age=d , identity=idd)
            return HttpResponseRedirect('/allrecord/')
        else:
            data=Customer(id=id, name=a ,lname=b , email=c ,age=d ,identity=idd,image=e)
            data.save()
            return HttpResponseRedirect('/allrecord/')
    d=Customer.objects.get(pk=id)
    return render(request,"app/update.html",{'data':d})
        
        


def delete(request,id):
    d=Customer.objects.get(pk=id)
    d.delete()
    # aa= "Delete Successfully!"    
    return redirect( 'allrecord' )  
    # return render(request,"app/allrecord.html")  




