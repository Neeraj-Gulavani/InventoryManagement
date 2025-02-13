from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# Create your views here.
def index(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('login:index'))
        else:
            return render(request,'login/index.html',{
                "message": "Invalid Credentials"
            })
    if not request.user.is_authenticated:
        return render(request,'login/index.html')
    else:
        return HttpResponseRedirect(reverse('content:index'))
    
def logout_view(request):
    logout(request)
    return render(request,"login/index.html",{
        "message": "Logged Out."
    })