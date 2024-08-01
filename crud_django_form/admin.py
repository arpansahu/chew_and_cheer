from django.contrib import admin
from crud_django_form.models import Item


# Register your models here.

@admin.register(Item)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
