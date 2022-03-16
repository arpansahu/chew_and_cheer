from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from graphqlapp.schema import schema, schema2, schema_user_authentication
from .views import graphql_home, graphql_delete_item, graphql_update_item

urlpatterns = [

    path('', GraphQLView.as_view(graphiql=True, schema=schema)),
    path('query/', GraphQLView.as_view(graphiql=True, schema=schema2)),
    path('account/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema_user_authentication))),

    path('home/', graphql_home, name='graphql_home'),
    path('home/delete/<int:id>/', graphql_delete_item, name="graphql_delete"),
    path('home/update/<int:id>/', graphql_update_item, name="graphql_update"),
]
