from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.auth import CustomAuthtoken
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from api.views import (
    item_detail,
    item_detail_list,
    item_create,
    item_api,
    ItemApiClass,
    item_api_funview,
    ItemApiClassView,
    ItemList,  # throttling is also used here
    ItemCreate,  # throttling is also used here
    ItemDestroy,  # throttling is also used here
    ItemRetrive,  # throttling is also used here
    ItemUpdate,  # throttling is also used here
    ItemApiGeneric,
    ItemApiGenericId,
    ItemViewSet,
    ItemModelViewSet,
    ItemReadOnlyModelViewSet,
    ItemModelViewSetWithAuth,
    ItemModelViewSetWithSessionAuth,
    ItemModelViewSetWithCustomPermissions,
    ItemModelViewSetWithTokenAuthentication,
    ItemModelViewSetWithCustomAuthentication,
    ItemModelViewSetWithJWTAuthentication,
    ItemModelViewSetWithSessionAuthWithThrottling,
    ItemListWithFilters,
    ItemListWithDjangoFilters,
    ItemListWithDjangoSearchFilter,
    ItemListWithOrderingFilter,
    ItemListWithPagination,
    ItemListWithOffLimitPagination,
    ItemListWithCursorPagination,
    SingerViewSet,
    SongViewSet,
    ItemModelVieSetWithHyperLinkedSerializer,
    SingerNestedViewSet,
)

# Creating Router Object
router_view_set = DefaultRouter()
router_model_view_set = DefaultRouter()
router_readonly_model_view_set = DefaultRouter()
router_model_view_set_with_auth = DefaultRouter()
router_model_view_set_with_session_auth = DefaultRouter()
router_model_view_set_with_custom_permission = DefaultRouter()
router_model_view_set_with_token_authentication = DefaultRouter()
router_model_view_set_with_custom_authentication = DefaultRouter()
router_model_view_set_with_jwt_authentication = DefaultRouter()
router_model_view_set_with_session_auth_with_throttling = DefaultRouter()
router_model_view_set_with_serializer_relations = DefaultRouter()
router_model_view_set_with_hyperlinked_serializer = DefaultRouter()
router_model_view_set_with_nested_serializer = DefaultRouter()

# Register StudentViewSet with Router
router_view_set.register('item_router', ItemViewSet, basename='item_base')
router_model_view_set.register('item_router', ItemModelViewSet, basename='item_base')
router_readonly_model_view_set.register('item_router', ItemReadOnlyModelViewSet, basename='item_base')
router_model_view_set_with_auth.register('item_router', ItemModelViewSetWithAuth, basename='item_base')
router_model_view_set_with_session_auth.register('item_router', ItemModelViewSetWithSessionAuth,
                                                 basename='item_base')
router_model_view_set_with_custom_permission.register('item_router',
                                                      ItemModelViewSetWithCustomPermissions, basename='item_base')
router_model_view_set_with_token_authentication.register('item_router',
                                                         ItemModelViewSetWithTokenAuthentication, basename='item_base')
router_model_view_set_with_custom_authentication.register('item_router',
                                                          ItemModelViewSetWithCustomAuthentication,
                                                          basename='item_base')
router_model_view_set_with_jwt_authentication.register('item_router', ItemModelViewSetWithJWTAuthentication,
                                                       basename='item_base')
router_model_view_set_with_session_auth_with_throttling.register('item_router',
                                                                 ItemModelViewSetWithSessionAuthWithThrottling,
                                                                 basename='item_base')
router_model_view_set_with_serializer_relations.register('singer', SingerViewSet, basename='singer_base')
router_model_view_set_with_serializer_relations.register('song', SongViewSet, basename='song_base')
router_model_view_set_with_hyperlinked_serializer.register('item_router', ItemModelVieSetWithHyperLinkedSerializer,
                                                           basename='item_base')
router_model_view_set_with_nested_serializer.register('singer', SingerNestedViewSet, basename='singer_base')
router_model_view_set_with_nested_serializer.register('song', SongViewSet, basename='song_base')


urlpatterns =[
    path('api/itemdetail/<int:pk>', item_detail, name='api_item_detail'),
    path('api/itemdetail/', item_detail_list, name='api_item_detail_list'),
    path('api/itemcreate/', item_create, name='api_item_create'),
    path('itemapi', item_api, name='item_api'),
    path('itemapiclass', ItemApiClass.as_view(), name='item_api_class'),
    path('itemapifunview', item_api_funview, name='item_api_fun_view'),
    path('itemapifunview/<int:pk>/', item_api_funview, name='item_api_fun_view_with_id'),
    path('itemapiclassview', ItemApiClassView.as_view(), name='item_api_class_view'),
    path('itemapiclassview/<int:pk>/', ItemApiClassView.as_view(), name='item_api_class_view_with_id'),
    path('itemapigenericretrive', ItemRetrive.as_view(), name='item_api_generic_retrive'),
    path('itemapigenericlist', ItemList.as_view(), name='item_api_generic_view_list'),
    path('itemapigenericretrive/<int:pk>/', ItemRetrive.as_view(), name='item_api_generic_retrive_with_id'),
    path('itemapigenericcreate', ItemCreate.as_view(), name='item_api_generic_create'),
    path('itemapigenericupdate', ItemUpdate.as_view(), name='item_api_generic_update'),
    path('itemapigenericdelete', ItemDestroy.as_view(), name='item_api_generic_delete'),
    path('itemgeneric', ItemApiGeneric.as_view(), name='item_api_generic'),
    path('itemgeneric/<int:pk>/', ItemApiGenericId.as_view(), name='item_api_generic_with_id'),
    path('itemapiviewset', include(router_view_set.urls), name='item_api_view_set'),
    path('itemapimodelviewset', include(router_model_view_set.urls), name='item_api_model_view_set'),
    path('itemapireadonlymodelviewset', include(router_readonly_model_view_set.urls),
         name='item_api_read_only_model_vie_set'),
    path('itemapimodelviesetwithauth', include(router_model_view_set_with_auth.urls),
         name='item_api_model_view_set_with_auth'),
    path('itemapimodelviesetwithsessionauth', include(router_model_view_set_with_session_auth.urls),
         name='item_api_model_view_set_with_session_auth'),
    path('sessionrestlogin', include('rest_framework.urls', namespace='rest_framework')),
    path('itemapimodelviesetwithcustompermission', include(router_model_view_set_with_custom_permission.urls),
         name='item_api_model_view_set_with_custom_premissions'),
    path('gettoken/', obtain_auth_token),
    path('getcustomtoken/', CustomAuthtoken.as_view(), name="get_customauth_token"),
    path('itemapimodelviewsetwithtokenauth/', include(router_model_view_set_with_token_authentication.urls),
         name='item_api_model_view_set_with_token_authentication'),
    path('itemapimodelviewsetwithcustomauth/', include(router_model_view_set_with_custom_authentication.urls),
         name='item_api_model_view_set_with_custom_authentication'),
    path('gettokenjwt/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtokenjwt/', TokenRefreshView.as_view(), name='token_refresh_jwt'),
    path('verifytokenjwt/', TokenVerifyView.as_view(), name='token_verify'),
    path('itemapimodelviewsetwithjwtauth/', include(router_model_view_set_with_jwt_authentication.urls),
         name='item_api_model_view_set_with_jwt_auth'),
    path('itemapimodelviesetwithsessionauthwiththrottling/',
         include(router_model_view_set_with_session_auth_with_throttling.urls)
         , name='item_api_model_view_with_session_auth_with_throttling'),
    path('itemapilistwithfilter/', ItemListWithFilters.as_view(), name='item_api_list_view_with_filters'),
    path('itemaapilistwithdjangofilters/', ItemListWithDjangoFilters.as_view(),
         name='item_api_list_view_with_django_filters'),
    path('itemapilistwithdjangosearchfilters/', ItemListWithDjangoSearchFilter.as_view(),
         name='item_api_list_view_with_search_filters'),
    path('itemapilistwithdjangoorderingfilter/', ItemListWithOrderingFilter.as_view(),
         name='item_api_list_view_with_ordering_filter'),
    path('itemapilistwithpagination/', ItemListWithPagination.as_view(),
         name='item_api_list_view_with_pagination'),
    path('itemapilistwithofflimitpagination/', ItemListWithOffLimitPagination.as_view(),
         name='item_api_list_view_with_off_limit_pagination'),
    path('itemapilistwithcursorlimitpagination/', ItemListWithCursorPagination.as_view(),
         name='item_api_list_view_with_cursor_pagination'),
    path('api/serializerrelationship/', include(router_model_view_set_with_serializer_relations.urls),
         name='serializers_with_relationships'),
    path('api/hyperlinkedserializer/', include(router_model_view_set_with_hyperlinked_serializer.urls),
         name='serializers_with_hyperlinks'),
    path('api/nestedserializers/', include(router_model_view_set_with_nested_serializer.urls),
         name='nested_serializers'),
]