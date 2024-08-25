"""chew_and_cheer URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

auth_views.LoginView
from .views import (
    home,
    HomeClassView,

)

def trigger_error(request):
    division_by_zero = 1 / 0

def large_resource(request):
   time.sleep(4)
   return HttpResponse("Done!")

urlpatterns = [

    path('graphql/', include('graph_ql_app.urls')),

    path('admin/', admin.site.urls),

    # path('', home, name="home"),
    path('', HomeClassView.as_view(), name="home"),

    path('crud_django_forms/', include('crud_django_form.urls')),
    path('crud_ajax_class/', include('crud_ajax.urls')),

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
         
    #sentry test view 
    path('sentry-debug/', trigger_error),
    path('large_resource/', large_resource)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'account.views.error_404'
handler500 = 'account.views.error_500'
handler403 = 'account.views.error_403'
handler400 = 'account.views.error_400'
