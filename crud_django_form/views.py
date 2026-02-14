from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .forms import ItemCreation
from crud_django_form.models import Item


@login_required(login_url='login')
def home_views(request):
    """
    View for displaying and managing menu items using Django forms.
    Includes pagination and search functionality.
    """
    # Handle form submission for creating new items
    if request.method == 'POST':
        itemform = ItemCreation(request.POST)
        
        if itemform.is_valid():
            try:
                # Save the new item
                item = itemform.save()
                messages.success(request, f'Item "{item.name}" added successfully!')
                return redirect('crudformhome')
            except Exception as e:
                messages.error(request, f'Error adding item: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        itemform = ItemCreation()
    
    # Handle search
    search_query = request.GET.get('search', '')
    items = Item.objects.all().order_by('-id')
    
    if search_query:
        items = items.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Pagination
    items_per_page = request.GET.get('per_page', 5)
    try:
        items_per_page = int(items_per_page)
        if items_per_page not in [5, 10, 25, 50]:
            items_per_page = 5
    except (ValueError, TypeError):
        items_per_page = 5
    
    paginator = Paginator(items, items_per_page)
    page_num = request.GET.get('page', 1)
    
    try:
        page = paginator.page(page_num)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    
    context = {
        'form': itemform,
        'items': page,
        'search_query': search_query,
        'items_per_page': items_per_page,
        'total_items': items.count(),
    }
    
    return render(request, 'crud_django_form/Home.html', context)


@login_required(login_url='login')
@permission_required('admin.can_add_log_entry', login_url='logout')
def delete_item(request, id):
    """
    View for deleting a menu item.
    Requires admin permissions.
    """
    if request.method == 'POST':
        try:
            item = get_object_or_404(Item, pk=id)
            item_name = item.name
            item.delete()
            messages.success(request, f'Item "{item_name}" deleted successfully!')
        except Exception as e:
            messages.error(request, f'Error deleting item: {str(e)}')
    
    return redirect('crudformhome')


@login_required(login_url='login')
def update_item(request, id):
    """
    View for updating a menu item.
    """
    item = get_object_or_404(Item, pk=id)
    
    if request.method == 'POST':
        itemform = ItemCreation(request.POST, instance=item)
        if itemform.is_valid():
            try:
                updated_item = itemform.save()
                messages.success(request, f'Item "{updated_item.name}" updated successfully!')
                return redirect('crudformhome')
            except Exception as e:
                messages.error(request, f'Error updating item: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        itemform = ItemCreation(instance=item)
    
    context = {
        'form': itemform,
        'item': item,
        'is_update': True,
    }
    
    return render(request, 'crud_django_form/updateitem.html', context)
