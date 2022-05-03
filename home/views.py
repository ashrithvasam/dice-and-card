from django.shortcuts import render
from django.http import HttpResponse
from home.models import Register
# Create your views here.
def home(request):
  
    return render(request,"game.html")
   
def dice(request):
    return render(request,"dice.html")

def cards(request):
    return render(request,"cards.html")

def login(request):
    return render(request,"x.html")

def register(request):
    return render(request,"register.html")

def registration(request):
    if request.method=="POST":
        user=request.POST['user']
        email=request.POST['email']
        phno=request.POST['phno']
        p1=request.POST['pass']
        p2=request.POST['repass']
        if p1==p2:
            newrow=Register(Username=user,email=email,phone=phno,password=p1)
            newrow.save()
        return render(request,"register.html")

def login(request):
    return render(request,"x.html")

def verify(request):
    if request.method=="POST":
        user=request.POST.get('user')
        p=request.POST.get('pass')
        u=Register.objects.all().values('Username')
        passw=Register.objects.all().values('password')
        for i in range(0,len(u)):
            if u[i]['Username']==user and passw[i]['password']==p:
                return render(request,"game.html",{'user':user})
  
    else:
        return render(request,"x.html") 


