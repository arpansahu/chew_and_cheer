from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic.base import View


@login_required(redirect_field_name='')
def home(request):
    return render(request, 'Home.html')


@method_decorator(login_required(redirect_field_name=''), name='dispatch')
class HomeClassView(View):
    def get(self, request):
        return render(request, 'Home.html')
