from django.urls import path

from .views import (
    CrudView,
    CreateCrudUser,
    UpdateCrudUser,
    DeleteCrudUser,
)

urlpatterns = [
    path('ajax/crudclass', CrudView.as_view(), name='crud_ajax'),
    path('ajax/crudclass/create/', CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('ajax/crudclass/update/', UpdateCrudUser.as_view(), name='crud_ajax_update'),
    path('ajax/crudclass/delete/', DeleteCrudUser.as_view(), name='crud_ajax_delete'),
]