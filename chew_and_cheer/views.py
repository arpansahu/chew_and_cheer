from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from django.contrib import messages
from crud_django_form.models import Item
from django.db.models import Count
from rest_framework.schemas import get_schema_view as rest_get_schema_view
from django.http import HttpResponse


@login_required(redirect_field_name='')
def home(request):
    """
    Home view displaying dashboard statistics for authenticated users.
    """
    context = {}
    
    if request.user.is_authenticated:
        try:
            # Get statistics for dashboard
            total_items = Item.objects.count()
            context.update({
                'total_items': total_items,
                'welcome_message': f'Welcome back, {request.user.username}!',
            })
        except Exception as e:
            messages.error(request, 'Unable to load dashboard statistics.')
            
    return render(request, 'Home.html', context)


@method_decorator(login_required(redirect_field_name=''), name='dispatch')
class HomeClassView(View):
    """
    Class-based view for home page with enhanced functionality.
    """
    template_name = 'Home.html'
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    def get_context_data(self):
        """Prepare context data for the template."""
        context = {}
        
        if self.request.user.is_authenticated:
            try:
                # Get statistics
                total_items = Item.objects.count()
                
                context.update({
                    'total_items': total_items,
                    'welcome_message': f'Welcome back, {self.request.user.username}!',
                    'user': self.request.user,
                })
            except Exception as e:
                messages.error(self.request, 'Unable to load dashboard statistics.')
                
        return context


def custom_schema_view(request):
    """
    Custom view to render API schema in a beautiful HTML interface.
    """
    # Always return HTML view - YAML/JSON will be handled by separate URL
    return render(request, 'api_schema.html')
