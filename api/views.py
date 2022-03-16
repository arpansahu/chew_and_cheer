from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework import serializers
from rest_framework.serializers import Serializer
from cruddjangoform.models import Item
from .serializers import ItemSerializer, SingerSerializer, SongSerializer, ItemHyperLinkedSerializer, \
    SingerSerializerNested
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, DjangoModelPermissions, \
    DjangoModelPermissionsOrAnonReadOnly, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .custompermissions import MyPermissions
from .customauth import CustomAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import JackRateThrottle
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from .mypaginations import MyPageNumberPagination, MyLimitOffsetPagination, MyLimitCursoragination
from .models import Singer, Song


# Create your views here.

def item_detail(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(item)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type= 'application/json')
    return JsonResponse(serializer.data, safe=True)


def item_detail_list(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type= 'application/json')
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def item_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = ItemSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Item Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


@csrf_exempt
def item_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            item = Item.objects.get(id=id)
            serializer = ItemSerializer(item)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = ItemSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        item = Item.objects.get(id=id)
        #  Complete Update - Required All Data from Front End/Client
        #  serializer = ItemSerializer(item, data=pythondata) 
        #  Partial Update - All Data not required
        serializer = ItemSerializer(item, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated !!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        item = Item.objects.get(id=id)
        item.delete()
        res = {'msg': 'Data Deleted!!'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(res, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class ItemApiClass(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            item = Item.objects.get(id=id)
            serializer = ItemSerializer(item)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = ItemSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        item = Item.objects.get(id=id)
        #  Complete Update - Required All Data from Front End/Client
        #  serializer = ItemSerializer(item, data=pythondata) 
        #  Partial Update - All Data not required
        serializer = ItemSerializer(item, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated !!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        item = Item.objects.get(id=id)
        item.delete()
        res = {'msg': 'Data Deleted!!'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(res, safe=False)


# if permission needed to be included this needs to be in same order
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def item_api_funview(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            item = Item.objects.get(id=id)
            serializer = ItemSerializer(item)
            return Response(serializer.data)

        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = request.data.get('id')
        item = Item.objects.get(pk=id)
        serializer = ItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = request.data.get('id')
        item = Item.objects.get(pk=id)
        item.delete()
        return Response({'msg': 'Data Deleted'})


class ItemApiClassView(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            item = Item.objects.get(id=id)
            serializer = ItemSerializer(item)
            return Response(serializer.data)

        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        item = Item.objects.get(pk=id)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        item = Item.objects.get(pk=id)
        serializer = ItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        item = Item.objects.get(pk=id)
        item.delete()
        return Response({'msg': 'Data Deleted'})


# Generic API View
class ItemList(GenericAPIView, ListModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewitem'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ItemCreate(GenericAPIView, CreateModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifyitem'

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ItemRetrive(GenericAPIView, RetrieveModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewitem'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ItemUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifyitem'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ItemDestroy(GenericAPIView, DestroyModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifyitem'

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Concrete API View
# List and Create - PK Not Required
class ItemApiGeneric(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Retrieve Update and Destroy - PK Required
class ItemApiGenericId(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# ViewSet
class ItemViewSet(viewsets.ViewSet):
    def list(self, request):
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            item = Item.objects.get(id=id)
            serializer = ItemSerializer(item)
            return Response(serializer.data)

    def create(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk
        item = Item.objects.get(pk=id)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        id = pk
        item = Item.objects.get(pk=id)
        serializer = ItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        item = Item.objects.get(pk=id)
        item.delete()
        return Response({'msg': 'Data Deleted'})


class ItemModelViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# Django Rest Authentication
class ItemModelViewSetWithAuth(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes=[AllowAny]
    # permission_classes=[IsAdminUser]


class ItemModelViewSetWithSessionAuth(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes=[AllowAny]
    # permission_classes=[IsAdminUser]
    # permission_classes=[IsAuthenticatedOrReadOnly]
    # permission_classes=[DjangoModelPermissions]
    # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]


# Using Custom Permission
class ItemModelViewSetWithCustomPermissions(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermissions]


class ItemModelViewSetWithTokenAuthentication(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]


class ItemModelViewSetWithCustomAuthentication(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]


class ItemModelViewSetWithJWTAuthentication(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ItemModelViewSetWithSessionAuthWithThrottling(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes=[AllowAny]
    # permission_classes=[IsAdminUser]
    # permission_classes=[IsAuthenticatedOrReadOnly]
    # permission_classes=[DjangoModelPermissions]
    # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    throttle_classes = [AnonRateThrottle, JackRateThrottle]


class ItemListWithFilters(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.filter(id=72)


class ItemListWithDjangoFilters(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name']
    filterset_fields = ['name', 'description']


class ItemListWithDjangoSearchFilter(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [SearchFilter]
    filterset_fields = ['name']
    # filterset_fields = ['name', 'description']
    # search_fields = ['^name']


class ItemListWithOrderingFilter(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['name']


class ItemListWithPagination(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = MyPageNumberPagination


class ItemListWithOffLimitPagination(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = MyLimitOffsetPagination


class ItemListWithCursorPagination(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = MyLimitCursoragination


class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class ItemModelVieSetWithHyperLinkedSerializer(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemHyperLinkedSerializer


class SingerNestedViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SingerSerializerNested
