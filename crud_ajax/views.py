from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from crud_django_form.models import Item
from django.views.generic import View
from django.http import JsonResponse


@method_decorator(login_required(login_url='login'), name='dispatch')
class CrudView(ListView):
    model = Item
    template_name = 'crud_ajax/Home.html'
    context_object_name = 'items'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateCrudUser(View):
    def get(self, request):
        name = request.GET.get('name', None)
        description = request.GET.get('description', None)
        price = request.GET.get('price', None)

        obj = Item.objects.create(
            name=name,
            description=description,
            price=price
        )

        item = {'id': obj.id, 'name': obj.name, 'description': obj.description, 'price': obj.price}

        data = {
            'item': item
        }
        return JsonResponse(data)


@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateCrudUser(View):
    def get(self, request):
        id = request.GET.get('id', None)
        name = request.GET.get('name', None)
        description = request.GET.get('description', None)
        price = request.GET.get('price', None)

        obj = Item.objects.get(id=id)
        obj.name = name
        obj.description = description
        obj.price = price
        obj.save()

        item = {'id': obj.id, 'name': obj.name, 'description': obj.description, 'price': obj.price}

        data = {
            'item': item
        }
        return JsonResponse(data)

    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class DeleteCrudUser(View):
    def get(self, request):
        id = request.GET.get('id', None)
        Item.objects.get(id=id).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

    @method_decorator(permission_required('admin.can_add_log_entry', login_url='logout'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
