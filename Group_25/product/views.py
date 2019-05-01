from django.shortcuts import render, HttpResponseRedirect, reverse
from product.models import Cuisine_item,Menu
from django.shortcuts import get_object_or_404
from product.forms import ProductForm
from django.db import connection
# Create your views here.


def show_menu(request):

    categories = Menu.objects.all()
    context = {
        'categories':categories,
    }

    return render(request, 'product/base_menu.html', context=context)


def category_items(request, category_id):

    category_name = get_object_or_404(Menu, pk=category_id)
    item_id = category_name.id
    items = Cuisine_item.objects.raw('SELECT * from product_cuisine_item where item_category_id=%s', [item_id])
    context = {
        'items':items, 'category_name':category_name,
    }
    return render(request, 'product/base_items.html', context=context)


def add_product(request):

    if request.method == 'POST':

        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('product:add_product'))
        else:
            print(product_form.errors)
    else:
        product_form = ProductForm()
        return render(request, 'product/add_product.html', {'product_form': product_form})