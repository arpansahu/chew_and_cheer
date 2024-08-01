from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View

from .forms import ItemCreation
from crud_django_form.models import Item
from django.core.paginator import Paginator, EmptyPage


# Create your views here.

# Funciton for showing all items in menu and adding new items
def home_views(request):
    if request.POST:
        itemform = ItemCreation(request.POST)

        if itemform.is_valid():

            # Using Model Class Object
            cond = False
            if cond:
                itemformname = itemform.cleaned_data['name']
                itemformdesc = itemform.cleaned_data['description']
                itemformprice = itemform.cleaned_data['price']
                addingobj = Item(name=itemformname, description=itemformdesc, price=itemformprice)
                addingobj.save()

            # Using Django Form
            else:
                itemform.save()
            itemform = ItemCreation()
    else:
        itemform = ItemCreation()

    items = Item.objects.all()
    # Paginator
    p = Paginator(items, 5)

    page_num = request.GET.get('page', 1)

    # print("Number of Pages")
    # print(p.num_pages)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    return render(request, 'crud_django_form/Home.html', {'form': itemform, 'items': page})


# This function will delete an item from the menu
@permission_required('admin.can_add_log_entry', login_url='logout')
def delete_item(request, id):
    if request.POST:
        item = Item.objects.get(pk=id)
        item.delete()
        return redirect('crudformhome')


# This function will edit an item from the menu
def update_item(request, id):
    if request.POST:
        item = Item.objects.get(pk=id)
        itemform = ItemCreation(request.POST, instance=item)
        if itemform.is_valid():
            itemform.save()
        return redirect('crudformhome')
    else:
        item = Item.objects.get(pk=id)
        itemform = ItemCreation(instance=item)
    return render(request, 'crud_django_form/updateitem.html', {'form': itemform})
