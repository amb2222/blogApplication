from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import generic
from .forms import ProductForm 


class IndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'products'
    model = Product
    
    
class DetailView(generic.DetailView):
    template_name = 'blogs/detail.html'
    context_object_name = 'product'
    model = Product
    
    
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'blogs/create.html', {'form': form})


def modify(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'blogs/modify.html', {'form': form})


def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'blogs/delete.html', {'product': product})