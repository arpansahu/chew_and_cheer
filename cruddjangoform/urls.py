from django.urls import path

from cruddjangoform.views import (
    home_views,
    delete_item,
    update_item,
)

urlpatterns = [
    path('crudformHome', home_views, name="crudformhome"),
    path('crudformdelete/<int:id>/', delete_item, name="curdformdelete"),
    path('crudformupdate/<int:id>/', update_item, name="curdformupdate"),
]