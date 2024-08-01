import json

from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from crud_django_form.forms import ItemCreation
from crud_django_form.models import Item
from .models import Quizzes

from .schema import schema, Query2
import graphene


def graphql_home(request):
    if request.POST:
        itemform = ItemCreation(request.POST)

        if itemform.is_valid():
            # Using Model Class Object

            itemformname = itemform.cleaned_data['name']
            itemformdesc = itemform.cleaned_data['description']
            itemformprice = itemform.cleaned_data['price']

            # result = schema.execute(
            #
            #     '''                mutation
            # zerothcrudMutation($name: String!, $description: String!, $price: Float!){
            #     createItem(name: $name, description: $description, price: $price){
            #     item
            # {
            #     name,
            #     description,
            #     price
            # }
            # }
            # }''',
            #     variables={'$name': graphene.String(itemformname), '$description': graphene.String(itemformdesc), '$price': graphene.Float(itemformprice)},
            # )
            # print(result, graphene.String(itemformname))

            # result = schema.execute(
            #     '''mutation zerothcrudMutation{createItem(name: "{namevar}", description: "{descriptionvar}", price: {pricevar}){item{name,description,price}}}'''.format(
            #         namevar=itemformname, descriptionvar=itemformdesc, pricevar=itemformprice)
            # )
            result = schema.execute(
                'mutation {createItem(name: "' + str(itemformname) + '",description: "' + str(itemformdesc) + '",price: ' + str(itemformprice) + '){item{name,description,price}}}''')

            print(result)
            itemform = ItemCreation()
    else:
        itemform = ItemCreation()

    items = schema.execute("query{allItems{id,name,description,price}}").to_dict()['data']['allItems']

    # Paginator
    p = Paginator(items, 5)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    return render(request, 'graphql/graphql_home.html', {'form': itemform, 'items': page})


@permission_required('admin.can_add_log_entry', login_url='logout')
def graphql_delete_item(request, id):
    if request.POST:
        result = schema.execute("mutation {deleteItem(id:"+str(id)+"){item{id}}}")
        print(result)
        return redirect('graphql_home')


# This function will edit an item from the menu
def graphql_update_item(request, id):
    if request.POST:
        item = Item.objects.get(pk=id)
        itemform = ItemCreation(request.POST, instance=item)
        if itemform.is_valid():

            itemformname = itemform.cleaned_data['name']
            itemformdesc = itemform.cleaned_data['description']
            itemformprice = itemform.cleaned_data['price']

            result = schema.execute(
                'mutation {updateItem(id:'+str(id)+',name: "' + str(itemformname) + '",description: "' + str(
                    itemformdesc) + '",price: ' + str(itemformprice) + '){item{name,description,price}}}''')


            print(result)
        return redirect('graphql_home')
    else:
        item = Item.objects.get(pk=id)
        itemform = ItemCreation(instance=item)
    return render(request, 'graphql/graphql_updateitem.html', {'form': itemform})
