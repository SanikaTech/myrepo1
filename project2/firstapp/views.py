from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def show(request):
    return render(request,'index.html')
def receive(request):
    if request.method=="POST":
       name=request.POST.get('name')
       email=request.POST.get('email')
       phone=request.POST.get('phone')
       message=request.POST.get('message')
       z=Contact(name=name,email=email,phone=phone,message=message)
       z.save()
       return HttpResponse("<h1>Data Entered...</h1>")

    else:
        return HttpResponse("<h1>Invalid Request...</h1>")

def dologin(request):
    return render(request,'login.html')       

def extra(request):
   return render(request,'dogboarding.html')       
def  mycat(request):
   return render(request,'catboarding.html')   
def  mymeal(request):
   return render(request,'healthymeal.html') 
def  myhealth(request):
   return render(request,'healthcare.html')
def  myact(request):
   return render(request,'actexe.html')
def  myspa(request):
   return render(request,'spagromming.html')     
def  myorder(request):
   return render(request,'order.html')       

def dosignup(request):
    return render(request,'signup.html')       

def myinfo(request):
    return render(request,'info.html')      

def showfeedback(request):
   return render(request,'feedback.html')

def conreport(request):
   con=Contact.objects.all()
   return render(request,'report.html',{'con':con})



def dofeedback(request):
    if request.method=="POST":
      name=request.POST.get('uname')   
      email=request.POST.get('email')   
      phone=request.POST.get('phone')   
      isSatisfied=request.POST.get('satisfy') 
      suggestion=request.POST.get('msg') 
      z=Feedback(name=name,email=email,phoneno=phone,isSatisfied=isSatisfied,suggestion=suggestion)    
      z.save()
      return HttpResponse("<h1>Thanks For Sharing Feedback...</h1>")
    else:
      return HttpResponse("<h1>Invalid Request....</h1>")

def takesignup(request):
    if request.method=="POST":
      name=request.POST.get('name')   
      email=request.POST.get('email')   
      dob=request.POST.get('bday')  
      phone=request.POST.get('phno')   
      z=Signup(name=name,email=email,date=dob,phoneno=phone)    
      z.save()
      return HttpResponse("<h1>You Are Registered.</h1>")
    else:
      return HttpResponse("<h1>Invalid Request....</h1>")
    

def takelogin(request):
    if request.method=="POST":
       
      username=request.POST.get('username')   
      password=request.POST.get('pwd')  
    
      z=Login(username=username,password=password)    
      z.save()
      return HttpResponse("<h1>You Are Logged In....</h1>")
    else:
      return HttpResponse("<h1>Invalid Request....</h1>")


def  getorder(request):
      if request.method=="POST":
          fname=request.POST.get('fname')   
          lname=request.POST.get('lname')   
          state=request.POST.get('state') 
          address=request.POST.get('addr')     
          city=request.POST.get('city')
          hometown=request.POST.get('hmtn')
          pincode=request.POST.get('pin')
          phone=request.POST.get('phone')
          email=request.POST.get('email') 
          productname=request.POST.get('prdct')
          price=request.POST.get('price')                    
          z=Order(fname=fname,lname=lname,state=state,address=address,city=city,hometown=hometown,pincode=pincode,phone=phone,email=email,productname=productname,price=price)    
          z.save()
          return HttpResponse("<h1>Your Order Is Successfull....</h1>")
      else:
          return HttpResponse("<h1>Invalid Request....</h1>")


def logreport(request):
   log=Login.objects.all()
   return render(request,'loginreport.html',{'log':log})



















    