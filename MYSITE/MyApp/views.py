from venv import logger
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
import logging
from django.shortcuts import get_object_or_404
# Create your views here.
 
logger = logging.getLogger(__name__)
# @login_required
# @cache_page(60)
# @vary_on_headers("User-agent")

def index(request):
    logger.info("Index view accessed.")
    item_list = Item.objects.all()
    logger.debug(f"Found {item_list.count()} items in the database.")
    paginator = Paginator(item_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request,"MyApp/index.html", context)

# class IndexClassView(ListView):
#     model = Item
#     template_name = "MyApp/index.html"
#     context_object_name = 'item_list'

def detail(request, id):
    logger.info(f"Detail view accessed for item id: {id}.")
    try:
        item = get_object_or_404(Item, pk=id)
        # item = Item.objects.get(id=id)
        logger.debug(f"Item found: {item}.")
    except Exception as e:
        # logger.error(f"Error retrieving item with id {id}: {e}")
        logger.error("Error retrieving item with id : ", id, e)
        raise
    
    context ={
        'item':item
    }
    return render(request, 'MyApp/detail.html', context)

# class FoodDetail(DetailView):
#     model = Item
#     template_name = "MyApp/detail.html"
#     context_object_name = 'item'

# def create_item(request):
#     form = ItemForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('MyApp:index') 

#     context = {
#         'form': form
#     }
#     return render(request, 'MyApp/item-form.html', context)

class ItemCreateView(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# def update_item(request, id):
#     item = Item.objects.get(id=id)
#     form = ItemForm(request.POST or None, instance=item)
#     if form.is_valid():
#         form.save()
#         return redirect('MyApp:index')
#     context = {
#         'form': form
#     }
#     return render(request, 'MyApp/item-form.html', context)

class ItemUpdateView(UpdateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name_suffix = '_update_form'

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

# def delete_item(request, id):
#     item = Item.objects.get(id=id)
#     if request.method == 'POST':
#         item.delete()
#         return redirect('MyApp:index')
#     return render(request, 'MyApp/item-delete.html')

class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('MyApp:index')

# def get_object(request):
#     for item in Item.objects.all():
#         print(item.item_name)


# def get_object_otimized(request):
#     items = Item.objects.all()
#     for item in items:
#         print(item.item_name)