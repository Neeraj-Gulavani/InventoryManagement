from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Asset
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login:index'))
    return render(request,'content/index.html', {
        "inventory": Asset.objects.all()
    })

def add_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login:index'))
    if request.method=="POST":
        name = request.POST["nameInput"]
        count = request.POST["countInput"]
        cost = request.POST["costInput"]
        price=request.POST["priceInput"]
        assetCall = Asset(name=name,count=count,cost=cost,price=price)
        assetCall.save()
        return HttpResponseRedirect(reverse('content:index'))
    return render(request,'content/add.html')

def edit_view(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login:index'))
    
    #item = Asset.objects.get(id=id)
    item = get_object_or_404(Asset, id=id)
    if request.method=="POST":
        item.name = request.POST["nameInput"]
        item.count = request.POST["countInput"]
        item.cost = request.POST["costInput"]
        item.price=request.POST["priceInput"]
        item.save()
        return HttpResponseRedirect(reverse('content:index'))

    if item:
        return render(request,'content/edit.html',{
            "item": item
        })
        

def delete_view(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login:index'))
    item = Asset.objects.filter(id=id).first()
    if item:
        item.delete()
        return render(request,'content/index.html', {
        "inventory": Asset.objects.all(),
        "message": "Successfully Deleted the item"
            })
    else:
        return render(request,'content/index.html', {
        "inventory": Asset.objects.all(),
        "message": "Couldn't Delete the item"
            })