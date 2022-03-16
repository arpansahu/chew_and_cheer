"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

auth_views.LoginView
from .views import (
    home,
    HomeClassView,

)

urlpatterns = [

    path('graphql/', include('graphqlapp.urls')),

    path('admin/', admin.site.urls),

    # path('', home, name="home"),
    path('', HomeClassView.as_view(), name="home"),

    path('crud_django_forms/', include('cruddjangoform.urls')),
    path('crud_ajax_class/', include('crudajax.urls')),

    path('api/v0/', include('api.urls')),
    # API schema and Documentation
    path('project/docs/', include_docs_urls(title='djangoProjectApis')),
    path('project/schema/', get_schema_view(
        title="BlogAPI",
        description="API for the "
                    "django Project APIs",
        version="1.0.0"
    ), name='openapi-schema'),

    path('accounts/', include('account.urls')),
]

handler404 = 'account.views.error_404'
handler500 = 'account.views.error_500'
handler403 = 'account.views.error_403'
handler400 = 'account.views.error_400'
