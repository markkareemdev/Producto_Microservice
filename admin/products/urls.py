from django.urls import path
from rest_framework import routers
from .views import ProductViewSet, UserViewSet




# router = routers.DefaultRouter()
# router.register(r'products', ProductViewSet)

urlpatterns = [

    # products

    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),


    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),


    # user

    path('product-user', UserViewSet.as_view({
        'get': 'list',
        'post': 'create'

        
    })),



]