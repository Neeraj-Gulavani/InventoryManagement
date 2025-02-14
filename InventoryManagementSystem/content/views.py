from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from .models import Asset
from django.contrib import messages
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login:index'))
    inventory = Asset.objects.filter(user=request.user)
    
    paginator = Paginator(inventory,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'content/index.html', {
        "inventory": page_obj
    })

def add_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login:index'))
    if request.method=="POST":
        name = request.POST["nameInput"]
        count = request.POST["countInput"]
        cost = request.POST["costInput"]
        price=request.POST["priceInput"]
        assetCall = Asset(user=request.user,name=name,count=count,cost=cost,price=price)
        assetCall.save()
        return HttpResponseRedirect(reverse('content:index'))
    return render(request,'content/add.html')

def edit_view(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login:index'))
    
    #item = Asset.objects.get(id=id)
    item = get_object_or_404(Asset, id=id,user=request.user)
    if request.method=="POST":
        item.name = request.POST["nameInput"]
        item.count = request.POST["countInput"]
        item.cost = request.POST["costInput"]
        item.price=request.POST["priceInput"]
        item.save()
        messages.success(request,"Successfully Edited " + item.name)
        return HttpResponseRedirect(reverse('content:index'))

    if item:
        return render(request,'content/edit.html',{
            "item": item
        })
        

def delete_view(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login:index'))
    item = Asset.objects.filter(id=id,user=request.user).first()
    if item:
        item.delete()
        messages.success(request, "Successfully deleted " + item.name)
        return HttpResponseRedirect(reverse('content:index'))
    else:
        messages.error(request,"Failed to Delete.")
        return HttpResponseRedirect(reverse('content:index'))