from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list':item_list
    }
    return render(request,"MyApp/index.html", context)

def detail(request, id):
    item = Item.objects.get(id=id)
    context ={
        'item':item
    }
    return render(request, 'MyApp/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('MyApp:index') 

    context = {
        'form': form
    }
    return render(request, 'MyApp/item-form.html', context)

def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('MyApp:index')
    context = {
        'form': form
    }
    return render(request, 'MyApp/item-form.html', context)

def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('MyApp:index')
    return render(request, 'MyApp/item-delete.html')